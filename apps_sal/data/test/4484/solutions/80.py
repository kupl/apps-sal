(n, m) = [int(i) for i in input().split()]
new_n = min(n, m)
new_m = max(n, m)
mod = 10 ** 9 + 7


def ans(n, m):
    if n == m:
        return 2 * kaijyou(n, mod) * kaijyou(m, mod)
    elif m - n == 1:
        return kaijyou(n, mod) * kaijyou(m, mod)
    else:
        return 0


def kaijyou(n, mod):
    ans = 1
    for i in range(1, n + 1):
        ans *= i
        ans = ans % mod
    return ans


print(ans(new_n, new_m) % mod)
