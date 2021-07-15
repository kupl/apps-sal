x, k = [int(v) for v in input().split()]
mod = 10**9 + 7

if x == 0:
    print(0)
else:
    print(((pow(2, k + 1, mod) * x) - (pow(2, k, mod) - 1)) % mod)

