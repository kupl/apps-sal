def main():
    import sys
    def input(): return sys.stdin.readline().rstrip()
    n, m = map(int, input().split())
    r = m // 2
    s = 1
    e = 2 * r + 1
    for _ in range(r):
        print(s, e)
        s += 1
        e -= 1

    s = n - 2 * (m - r) + 1
    e = n
    for _ in range(m - r):
        print(s, e)
        s += 1
        e -= 1


def __starting_point():
    main()


__starting_point()
