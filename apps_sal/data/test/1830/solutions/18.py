N, M = map(int, input().split())

r = N
c = N

R = [False for i in range(N)]
C = R.copy()

for i in range(M):
    a, b = map(int, input().split())

    if not R[a - 1]:
        r -= 1
        R[a - 1] = True

    if not C[b - 1]:
        c -= 1
        C[b - 1] = True

    print(r * c, end=' ')
