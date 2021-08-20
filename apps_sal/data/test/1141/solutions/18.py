def main():
    (n, m) = map(int, input().split())
    s = list(input())
    for i in range(m):
        (l, r, c1, c2) = input().split()
        l = int(l)
        r = int(r)
        for i in range(l - 1, r):
            if s[i] == c1:
                s[i] = c2
    print(''.join(s))


def __starting_point():
    try:
        main()
    except KeyboardInterrupt:
        pass


__starting_point()
