def factorial(n, mod):
    num = 1
    for i in range(1, n + 1):
        i %= mod
        num *= i
        num %= mod
    return num


def main():
    n, m = map(int, input().split())
    md = 10 ** 9 + 7

    if abs(n - m) >= 2:
        ans = 0
    elif abs(n - m) == 1:
        ans = (factorial(n, md) * factorial(m, md))
        ans %= md
    else:
        ans = (factorial(n, md) * factorial(m, md)) * 2
        ans %= md

    print(ans)


def __starting_point():
    main()
__starting_point()
