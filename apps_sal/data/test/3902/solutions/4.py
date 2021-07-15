def main():
    s = input()[5:]
    n = len(s)
    if n < 2:
        print(0)
        return
    res2, res3 = set(), set()
    dp2 = [False] * (n + 1)
    dp3 = [False] * (n + 1)
    dp2[-1] = dp3[-1] = True
    for i in range(n, 1, -1):
        if dp3[i] or dp2[i] and s[i - 2:i] != s[i:i + 2]:
            res2.add(s[i - 2:i])
            dp2[i - 2] = True
        if dp2[i] or dp3[i] and s[i - 3:i] != s[i:i + 3]:
            res3.add(s[i - 3:i])
            dp3[i - 3] = True
    res3.discard(s[i - 3:i])
    res3.update(res2)
    print(len(res3))
    for s in sorted(res3):
        print(s)


def __starting_point():
    main()

__starting_point()
