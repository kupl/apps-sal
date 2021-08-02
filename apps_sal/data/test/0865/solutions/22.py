from numpy import*
N, T, *AB = map(int, open(0).read().split())
dp = zeros(6010, int)
for w, v in sorted(zip(*[iter(AB)] * 2)): dp[w:T + w] = maximum(dp[w:T + w], dp[:T] + v)
print(max(dp))
