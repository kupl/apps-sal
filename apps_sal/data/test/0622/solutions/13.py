(n, k) = list(map(int, input().split()))


def nk(n, k):
    if n == 1:
        return 1
    t = 2 ** (n - 1)
    if k == t:
        return n
    if k < t:
        return nk(n - 1, k)
    else:
        return nk(n - 1, k - t)


print(nk(n, k))
