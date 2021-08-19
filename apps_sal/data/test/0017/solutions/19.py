(n, k, t) = list(map(int, input().split(' ')))


def main():
    if t < k:
        return t
    elif k <= t <= n:
        return k
    else:
        return n + k - t


print(main())
