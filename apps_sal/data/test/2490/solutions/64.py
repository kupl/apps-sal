L = list(map(int,list(input())))
L = [0] + L
N = len(L)
dp1 = [0 for _ in range(N+1)]
dp2 = [0 for _ in range(N+1)]

for i in range(N):
    dp1[i+1] = min(dp1[i] + L[i], dp2[i] + 10 - L[i])
    dp2[i+1] = min(dp2[i] + 10 - L[i] - 1, dp1[i] + L[i] + 1)

print(dp1[-1])
