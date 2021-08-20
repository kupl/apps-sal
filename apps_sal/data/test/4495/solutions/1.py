(a, b, x) = map(int, input().split())


def divided_num(n):
    return n // x + 1


print(divided_num(b) - divided_num(a) + (1 if a % x == 0 else 0))
