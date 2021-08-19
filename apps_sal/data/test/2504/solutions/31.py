from scipy.sparse.csgraph import floyd_warshall
(N, M, L) = map(int, input().split())
d = [[float('inf') for i in range(N)] for j in range(N)]
answer_d = [[float('inf') for i in range(N)] for j in range(N)]
for i in range(M):
    (A, B, C) = map(int, input().split())
    d[A - 1][B - 1] = d[B - 1][A - 1] = C
for i in range(N):
    d[i][i] = 0
d = floyd_warshall(d)
for i in range(N):
    for j in range(N):
        if d[i][j] <= L:
            answer_d[i][j] = answer_d[j][i] = 1
d = floyd_warshall(answer_d)
Q = int(input())
answer = [-1] * Q
for i in range(Q):
    (s, t) = map(int, input().split())
    if d[s - 1][t - 1] != float('inf'):
        answer[i] = d[s - 1][t - 1] - 1
for i in answer:
    print(i)
