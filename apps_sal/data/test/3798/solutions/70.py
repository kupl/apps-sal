import collections


def f(n, b):
    ret = int()
    while n > 0:
        ret += n % b
        n //= b
    return ret


def solve():
    n = int(input())
    s = int(input())
    b = int(2)
    while b * b <= n:
        if f(n, b) == s:
            print(b)
            return
        b += 1
    b = 0
    a = int(1)
    while a * a <= n - s:
        if (n - s) % a == 0 and\
            (n - s) // a >= a and\
            (s - a) >= 0 and\
                (n - s) // a >= (s - a):
            b = (n - s) // a + 1
            # print(b,s-a)
        a += 1
    if b > 0:
        print(b)
        return
    if n == s:
        print((n + 1))
        return
    print((-1))
    return


def __starting_point():
    solve()


__starting_point()
