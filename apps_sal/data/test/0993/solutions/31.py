from collections import defaultdict
n,m = map(int,input().split())
a = list(map(int,input().split()))
"""
aの連続列がMの倍数であればいい
dp[j] := jの倍数になる総数.
"""
dp = defaultdict(lambda: 0)
dp[0] = 1
tmp = 0
ans = 0
for i in range(n):
	tmp += a[i]
	ans += dp[tmp%m]
	dp[tmp%m] += 1
print(ans)
