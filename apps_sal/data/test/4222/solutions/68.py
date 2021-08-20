(N, K) = map(int, input().split())
d = []
A = []
for i in range(K):
    p = int(input())
    q = [int(i) for i in input().split()]
    d.append(p)
    A.append(q)
S = [False] * N
for i in range(K):
    for j in range(d[i]):
        S[A[i][j] - 1] = True
print(S.count(False))
