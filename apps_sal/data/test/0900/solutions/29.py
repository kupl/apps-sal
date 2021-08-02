def main():
    s = ''.join(reversed(input()))
    multiplier = 1
    divisor = 10 ** 9 + 7
    list10 = list(range(10))
    list13 = list(range(13))
    p = [0 for i in list13]
    np = [0 for i in list13]
    rt = [i % 13 for i in range(100)]
    if s[0] != '?':
        p[int(s[0])] = 1
    else:
        for j in range(10):
            p[j] = 1
    for i in range(1, len(s)):
        multiplier = (10 * multiplier) % 13
        if s[i] != '?':
            r = int(s[i]) * multiplier
            for j in list13:
                np[(j + r) % 13] = p[j]
        else:
            for j in range(10):
                r = multiplier * j % 13
                for k in list13:
                    np[rt[k + r]] += p[k]
        for j in list13:
            p[j] = np[j] % divisor
            np[j] = 0
    print(p[5] % divisor)


main()
