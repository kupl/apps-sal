from itertools import product

h, w, k = list(map(int, input().split()))
mod = 10 ** 9 + 7

dp = [[0] * w for _ in range(h + 1)]
dp[0][0] = 1

pats = [pat for pat in product([1, 0], repeat=w-1)]

for i in range(h):
	for j in range(w):
		for pat in pats:
			valid = True
			for e1, e2 in zip(pat, pat[1:]):
				if e1 and e2:
					valid = False

			if not valid:
				continue

			if j - 1 >= 0 and pat[j-1]:
				dp[i+1][j-1] += dp[i][j]
				dp[i+1][j-1] %= mod

			elif j <= w - 2 and pat[j]:
				dp[i+1][j+1] += dp[i][j]
				dp[i+1][j+1] %= mod

			else:
				dp[i+1][j] += dp[i][j]
				dp[i+1][j] %= mod

ans = dp[h][k-1]
print(ans)
#print(*dp, sep="\n")

