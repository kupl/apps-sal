(n, k) = map(int, input().split())


def f(i, j):
    l = 1 << i - 1
    if j == l:
        return i
    elif j < l:
        return f(i - 1, j)
    else:
        return f(i - 1, l - (j - l))


print(f(n, k))
