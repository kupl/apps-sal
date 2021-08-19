(n, m) = list(map(int, input().split()))
mod = 10 ** 9 + 7


def fact(n, mod):
    ans = 1
    for i in range(2, n + 1):
        ans = ans * i
        ans = ans % mod
    return ans


if abs(n - m) >= 2:
    print(0)
elif abs(n - m) == 1:
    print(fact(n, mod) * fact(m, mod) % mod)
elif abs(n - m) == 0:
    print(2 * fact(n, mod) * fact(m, mod) % mod)
