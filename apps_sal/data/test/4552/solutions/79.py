N = int(input())
F = [0] * N
for i in range(N):
    F[i] = list(map(int, input().split()))

P = [0] * N
for i in range(N):
    P[i] = list(map(int, input().split()))

ans = - 10 ** 10
for i in range(1, 2 ** 10):
    open_n = [0] * N
    profit = 0
    for j in range(10):
        if ((i >> j) & 1):
            for k in range(N):
                if F[k][j] == 1:
                    open_n[k] += 1
    for l in range(N):
        profit += P[l][open_n[l]]
    if ans < profit:
        ans = profit

print(ans)
