
def main():
    n, a, b, c, d = [int(x) for x in input().split()]
    cnt = 0
    for x in range(1, n + 1):
        z1 = x + b - c
        z2 = x + a + b - d - c
        z3 = x + a - d

        if all(1 <= xx <= n for xx in (z1, z2, z3)):
            cnt += n

    print(cnt)


def __starting_point():
    main()


__starting_point()
