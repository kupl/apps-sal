def main():
    n = int(input())
    mi, ma = 10000000001, 0
    l = []
    for _ in range(n):
        a, b = map(int, input().split())
        if mi > a:
            mi = a
        if ma < b:
            ma = b
        l.append((a, b))
    l.append((mi, ma))
    idx = l.index((mi, ma))
    print(-1 if idx == n else idx + 1)


def __starting_point():
    main()
__starting_point()
