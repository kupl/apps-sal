import math


def read_input():
    n = int(input())
    s = int(input())
    return (n, s)


def f(b, n):
    if n < b:
        return n
    t = n // b
    m = n % b
    return f(b, t) + m


def submit():
    (n, s) = read_input()
    sqrtn = math.ceil(math.sqrt(n))
    if n == s:
        print(n + 1)
        return
    for i in range(2, sqrtn + 1):
        if f(i, n) == s:
            print(i)
            return
    for i in range(sqrtn - 1, 0, -1):
        p = i
        q = s - p
        (sho, mod) = divmod(n - q, p)
        if mod == 0:
            b = sho
        else:
            continue
        if q < b and p < b:
            if f(b, n) == s:
                print(b)
                return
    print(-1)


def __starting_point():
    submit()


__starting_point()
