N = int(input())
T = list(map(int, input().split()))
V = list(map(int, input().split()))
M = 2
dt = 1 / M
R = sum(T)
maxSpeeds = [10 ** 18] * (R * M + 1)
now = 0
for (t, v) in zip(T, V):
    for i in range(t * M + 1):
        maxSpeeds[now + i] = min(maxSpeeds[now + i], v)
    now += t * M
maxSpeeds[0] = 0
maxSpeeds[-1] = 0
for t in range(1, R * M + 1):
    maxSpeeds[t] = min(maxSpeeds[t - 1] + dt, maxSpeeds[t])
    maxSpeeds[-(t + 1)] = min(maxSpeeds[-t] + dt, maxSpeeds[-(t + 1)])
ans = 0
for (l, r) in zip(maxSpeeds, maxSpeeds[1:]):
    ans += (l + r) / M / 2
print(ans)
