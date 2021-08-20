def main():
    (k, p) = map(int, input().split())
    s = 0
    for i in range(1, k + 1):
        r = str(i)
        w = r[::-1]
        n = int(r + w)
        s += n
    print(s % p)


def __starting_point():
    try:
        main()
    except KeyboardInterrupt:
        pass


__starting_point()
