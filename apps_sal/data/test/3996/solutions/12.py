from functools import reduce
MOD = 10 ** 9 + 7
n, a = int(input()), map(int, input().split())
n = reduce(lambda x,y:(x*y)%(MOD-1), a, 1)
# 333333336 * 3 = 1
# 500000004 * 2 = 1
k = n % 2
q = (pow(2, n, MOD) * 500000004) % MOD
if k == 0:
 p = ((q + 1) * 333333336) % MOD
else:
 p = ((q - 1) * 333333336) % MOD
print("%d/%d" % (p, q))
