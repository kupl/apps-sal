def main():
    s = input()
    s_len = len(s)
    mod = 2019
    d = [0] * mod
    d[0] = 1
    rev_num = 0
    t = 1
    for i in reversed(s):
        rev_num += int(i) * t
        rev_num %= mod
        d[rev_num] += 1
        t *= 10
        t %= mod
    print(sum((i * (i - 1) // 2 for i in d)))


def __starting_point():
    main()


__starting_point()
