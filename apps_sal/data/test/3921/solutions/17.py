n = int(input())
a = list(map(int, input().split()))
dp = [1] * (n + 5)
tmax = [0 for _ in range(100005)]
p = [[] for _ in range(100005)]
p[1] = [1]
for i in range(2, 100001):
    if (not p[i]):
        for j in range(i, 100001, i):
            p[j].append(i)
for i in range(len(a)):
    dp[i] = max(tmax[j] for j in p[a[i]]) + 1
    for j in p[a[i]]: tmax[j] = max(tmax[j], dp[i])
print(max(dp))
