n, a, b = map(int, input().split())


def f(n, a, b):

    if (b > n // 2 and a <= n // 2) or (a > n // 2 and b <= n // 2):

        return 0

    if a > n // 2 and b > n // 2:

        return 1 + f(n // 2, a - n // 2, b - n // 2)

    if a <= n // 2 and b <= n // 2:

        return 1 + f(n // 2, a, b)


deg = 0

raund = f(n, a, b)

while n > 0:

    deg += 1

    n //= 2

if raund == 0:

    print('Final!')

else:

    print(deg - raund - 1)
