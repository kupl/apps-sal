(N, M, H) = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))
t = [list(map(int, input().split())) for i in range(N)]
for i in range(N):
    for j in range(M):
        if not t[i][j]:
            continue
        t[i][j] = min(B[i], A[j])
    print(' '.join(map(str, t[i])))
