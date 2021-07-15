def main():
    n, s, t = map(int, input().split())
    l = [None]
    l.extend(map(int, input().split()))
    for i in range(n):
        if s == t:
            print(i)
            return
        s = l[s]
    print(-1)


def __starting_point():
    main()
__starting_point()
