def main():

    def R(): return map(int, input().split())
    n, v = R()
    mlist = [0] * 3003
    for i in range(n):
        a, b = R()
        mlist[a] += b
    mlist2 = mlist[:]
    ans = 0
    for i in range(1, 3002):
        tmp = min(v, mlist[i])
        ans += tmp
        mlist[i + 1] += min(mlist[i] - tmp, mlist2[i])
    print(ans)


def __starting_point():
    main()


__starting_point()
