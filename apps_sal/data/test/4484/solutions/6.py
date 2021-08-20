(n, m) = list(map(int, input().split()))


def f(n):
    ans = n
    for i in range(1, n):
        ans *= i
        ans %= 1000000007
    return ans


if n == m:
    print(f(n) ** 2 * 2 % 1000000007)
elif n == m + 1 or m == n + 1:
    print(f(n) * f(m) % 1000000007)
else:
    print(0)
