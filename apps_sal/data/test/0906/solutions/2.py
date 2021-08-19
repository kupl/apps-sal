mod = 1000000007


def BinPow2(x, n):
    if n == 0:
        return 1
    if n % 2 == 0:
        return BinPow2(x * x % mod, n // 2) % mod
    else:
        return x * (BinPow2(x * x % mod, (n - 1) // 2) % mod) % mod


(n, m, k) = list(map(int, input().split()))
if k == -1 and n % 2 != m % 2:
    print(0)
else:
    print(BinPow2(2, (n - 1) * (m - 1)))
