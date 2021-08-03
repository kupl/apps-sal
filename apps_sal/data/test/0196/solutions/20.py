x, k = list(map(int, input().split()))
mod = 10**9 + 7
if x == 0:
    print(0)
else:
    print(((2 * x - 1) * pow(2, k, mod) + 1) % mod)
