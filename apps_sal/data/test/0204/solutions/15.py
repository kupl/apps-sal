from fractions import gcd


def __starting_point():
    a, b, x, y = list(map(int, input().split()))
    c = gcd(x, y)
    x, y = x // c, y // c
    answer = min(a // x, b // y)
    print(answer)


__starting_point()
