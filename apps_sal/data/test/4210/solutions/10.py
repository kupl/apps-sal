from collections import Counter

n, k = [int(x) for x in input().split()]
lst = [int(x) for x in input().split()]
lst2 = []

for i in range(n):
    lst2.append(((lst[i] % k), len(str(lst[i]))))

dp = [[] for i in range(12)]
for j in lst2:
    dp[j[1]].append(j[0])
for i in range(12):
    if len(dp[i]) > 0:
        dp[i] = Counter(dp[i])
ans = 0

for i in lst:
    for j in range(2, 12):
        v1 = ((i % k) * pow(10, j - 1)) % k
        if (k - v1) % k in dp[j - 1]:
            ans = ans + dp[j - 1][(k - v1) % k]

for i in lst:
    if int(str(i) + str(i)) % k == 0:
        ans = ans - 1

print(ans)
