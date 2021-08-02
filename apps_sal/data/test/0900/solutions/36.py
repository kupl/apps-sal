def main():
    MOD = 10 ** 9 + 7

    s = input()
    r = [0] * 13
    r[0] = 1
    p = 1
    for c in reversed(s):
        if c == '?':
            tank = []
            for x in range(10):
                x = x * p % 13
                tank.append(r[13 - x:] + r[:13 - x])
            r = list(map(sum, list(zip(*tank))))
            *r, = [x % MOD for x in r]

        else:
            x = int(c)
            x = x * p % 13
            r = r[13 - x:] + r[:13 - x]
        p = p * 10 % 13

    print((r[5]))


def __starting_point():
    main()


__starting_point()
