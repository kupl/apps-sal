def main():
    n, x = list(map(int, input().split()))
    f = []
    n = 1 << n
    cx = [0 for _ in range(n + 299)]
    for i in range(n):
        if Find_x(int(x ^ i), f) == False:
            f.append(i)
    print(len(f) - 1)
    for i in range(len(f) - 1):
        print(f[i] ^ f[i + 1], end=' ')


def Find_x(x, a):
    l = 0
    r = len(a) - 1
    while l <= r:
        m = int((l + r) / 2)
        if a[m] == x:
            return True
        if a[m] > x:
            r = m - 1
        else:
            l = m + 1
    return False


def __starting_point():
    main()


__starting_point()
