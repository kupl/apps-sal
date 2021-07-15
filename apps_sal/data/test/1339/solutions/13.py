def main():
    n = int(input())
    l, r = [], []
    for _ in range(n):
        a, b = map(int, input().split())
        l.append(a)
        r.append(b)
    m = min(l), max(r)
    for i, a in enumerate(zip(l, r)):
        if a == m:
            print(i + 1)
            return
    print(-1)


def __starting_point():
    main()
__starting_point()
