USE_STDIO = False
if not USE_STDIO:
    try:
        import mypc
    except:
        pass


def parse(s):
    r = 0
    for c in s:
        r |= 1 << ord(c) - ord('A')
    return r


def main():
    (n,) = list(map(int, input().split(' ')))
    INF = 1000000000
    mp = [0] + [INF] * 7
    for _ in range(n):
        (c, s) = input().split(' ')
        (c, s) = (int(c), parse(s))
        for i in range(8):
            mp[i | s] = min(mp[i | s], mp[i] + c)
    print(mp[-1] if mp[-1] < INF else -1)


def __starting_point():
    main()


__starting_point()
