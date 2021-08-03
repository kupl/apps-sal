def main():
    input()
    aa = list(map(int, input().split()))
    n = max(aa) + 1
    cnt = [0] * n
    for x in aa:
        cnt[x] += x
    a = b = 0
    for x in cnt:
        a, b = b, max(b, a + x)
    print(b)


def __starting_point():
    main()


__starting_point()
