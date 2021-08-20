from functools import reduce
MOD = 1000000007
print(reduce(lambda a, b: a * b % MOD, list(range(1, int(input()) + 1))))
