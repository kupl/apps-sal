def main():
    input()
    l = list(map(int, input().split()))
    (s, res) = (sum(l), 0)
    if not s % 3:
        s //= 3
        s2 = s * 2
        tot = t = 0
        del l[-1]
        for x in l:
            tot += x
            if tot == s2:
                res += t
            if tot == s:
                t += 1
    print(res)


def __starting_point():
    main()


__starting_point()
