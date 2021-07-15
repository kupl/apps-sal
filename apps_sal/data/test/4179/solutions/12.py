N, M, C, = map(int, input().split())
B = list(map(int, input().split()))
A = [tuple(map(int, input().split())) for _ in range(N)]

cnt = 0
for a in range(N):
    math_list = []
    for b in range(M):
        math_list.append(A[a][b] * B[b])
    if sum(math_list) + C > 0:
        cnt += 1

print(cnt)
