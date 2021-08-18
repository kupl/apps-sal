N = int(input())
t = list(map(int, input().split()))
v = list(map(int, input().split()))


N_INF = - 10 ** 15
DP = [[N_INF] * (102) for _ in range(100 * 200 + 2)]
DP[0][0] = 0
time = 1
for i in range(N):
    for j in range(time, time + t[i]):
        for k in range(0, v[i] + 1):
            if k == 0:
                DP[j][k] = max(DP[j - 1][0] + 0.25, DP[j - 1][1] + 1 / 2)
            elif k != v[i]:
                DP[j][k] = max(DP[j - 1][k - 1] + k - 1 / 2, DP[j - 1][k] + k + 0.25, DP[j - 1][k + 1] + k + 1 / 2)
            else:
                DP[j][k] = max(DP[j - 1][k - 1] + k - 1 / 2, DP[j - 1][k] + k)
    time += t[i]
print((DP[time - 1][0]))
