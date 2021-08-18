__author__ = 'Alexander'


def f(n, k):
    t = 2 ** (n - 1)

    if k == t:
        return n
    elif k < t:
        return f(n - 1, k)
    else:
        return f(n - 1, k - t)


n, k = map(int, input().split())

print(f(n, k))
