import itertools


def main():
    ans = 0
    ans1 = []
    s = input()
    t = input()
    ss = len(s)
    ts = len(t)
    for i in range(ss - ts + 1):
        for (j, x) in enumerate(s[0 + i:ts + i]):
            if t[j] == x:
                ans += 1
        ans1.append(ans)
        ans = 0
    print(ts - max(ans1))


def __starting_point():
    main()


__starting_point()
