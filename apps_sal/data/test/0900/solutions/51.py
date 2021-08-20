def main():
    s = input()
    mod = 10 ** 9 + 7
    table1 = [0] * 13
    table2 = [0] * 13
    table1[0] = 1
    pre = [[(10 * i + j) % 13 for j in range(10)] for i in range(13)]
    for l in s:
        for i in range(13):
            q = table1[i] % mod
            if q == 0:
                continue
            if l == '?':
                for k in pre[i]:
                    table2[k] += q
            else:
                k = (10 * i + int(l)) % 13
                table2[k] += q
        table1 = table2
        table2 = [0] * 13
    print(table1[5] % mod)


def __starting_point():
    main()


__starting_point()
