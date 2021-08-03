from functools import reduce
MOD = 1_000_000_007
print((reduce(lambda a, b: a * b % MOD, list(range(1, int(input()) + 1)), 1)))
