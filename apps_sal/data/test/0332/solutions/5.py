(N, M) = list(map(int, input().split()))
A = [[int(a) for a in input().split()] for _ in range(N)]
B = [[int(a) for a in input().split()] for _ in range(N)]
AA = [[] for _ in range(N + M - 1)]
BB = [[] for _ in range(N + M - 1)]
for n in range(N):
    for m in range(M):
        AA[n + m].append(A[n][m])
        BB[n + m].append(B[n][m])
for i in range(N + M - 1):
    AA[i] = sorted(AA[i])
    BB[i] = sorted(BB[i])
    if AA[i] != BB[i]:
        print('NO')
        break
else:
    print('YES')
