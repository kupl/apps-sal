from collections import defaultdict
n,k = map(int,input().split())
a = list(map(int,input().split()))
ruisekiwa = [0 for _ in range(n+1)]
for i in range(n):
	ruisekiwa[i+1] = (ruisekiwa[i] + a[i] - 1) % k
dp = defaultdict(lambda: 0)
ans = 0
tmp = 0
for i in range(n+1):
	tmp += 1
	if tmp > k:
		dp[ruisekiwa[i-k]] -= 1
	ans += dp[ruisekiwa[i]]
	dp[ruisekiwa[i]] += 1
print(ans)
