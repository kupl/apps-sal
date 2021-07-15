

x,k = map(int, input().strip().split())

MOD = 1000000007

if x > 0:
	r = (pow(2, k+1, MOD) * x - pow(2, k, MOD) + 1 + MOD * 10) % MOD
else:
	r = 0

print(r)
