import math


def f(b, n):
    if n < b:
        return n
    else:
        return f(b, n // b) + n % b


def main():
    n = int(input())
    s = int(input())
    if s == n:
        print(n + 1)
        return
    elif s > n:
        print(-1)
        return
    sqrt = int(math.sqrt(n))
    for b in range(2, sqrt + 2):
        if f(b, n) == s:
            print(b)
            return
    for x in range(sqrt, 0, -1):
        if x > s:
            continue
        y = s - x
        b = (n - y) // x
        if b >= 2 and (n - y) % x == 0 and (f(b, n) == s):
            print(b)
            return
    print(-1)


def __starting_point():
    main()


__starting_point()
