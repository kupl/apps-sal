from collections import Counter
n = int(input())
a = list(map(int, input().split()))
a.sort()
dp = [0] * a[-1]
c = Counter(a)
for i in a:
    for j in range(i, a[-1] + 1, i):
        dp[j - 1] += 1
ans = 0
for i in a:
    if dp[i - 1] == 1 and c[i]:
        ans += 1
print(ans)
