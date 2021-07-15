x, k = [int(x) for x in input().split()]

if x == 0:
    print(0)
    return

mod = 10 ** 9 + 7

res = x * pow(2, k + 1, mod) % mod
res = ((res - (pow(2, k, mod) - 1)) % mod + mod) % mod

print(res)

