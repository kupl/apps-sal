n, m, k = list(map(int, input().split()))
mod = 998244353

same_bricks = n - 1 - k
total = m # First brick
# Different bricks
for i in range(k):
	total *= (m-1)
	total %= mod

# Choosing same bricks
# times (n-1 choose k)
val = 1
for i in range(n - k, n):
	val *= i

for i in range(1, k+1):
	val //= i

total *= val
total %= mod
print(total)

