import sys

MAX = 1000000


def digit_sum(n, b):
    if n == 0:
        return 0
    else:
        return digit_sum(n // b, b) + n % b


def main():
    n = int(input())
    s = int(input())

    if n < s:
        print((-1))
        return

    ans = -1

    for b in range(2, min(n + 1, MAX) + 1):
        sm = digit_sum(n, b)
        if sm == s:
            ans = b
            break

    if ans != -1:
        print(ans)
        return

    if n + 1 <= MAX:
        print((-1))
        return

    for p in reversed(list(range(1, MAX))):
        if (n - s) % p != 0:
            continue
        b = (n - s) // p + 1
        if b < 2:
            continue
        sm = digit_sum(n, b)
        if sm == s:
            ans = b
            break

    if ans != -1:
        print(ans)
        return

    if n == s:
        print((n+1))
        return

    print((-1))


def __starting_point():
    main()

__starting_point()
