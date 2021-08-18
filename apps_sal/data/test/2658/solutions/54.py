def main():
    n, k = map(int, input().split())
    a = [int(i) - 1 for i in input().split()]
    visit = [False] * n
    visit[0] = True
    loop, loopstart, loopout, cur = 0, -1, False, 0
    i = 0
    while i < k:
        cur = a[cur]
        if not loopout and visit[cur]:
            if loopstart == cur:
                k = (k - sum(visit)) % loop
                loopout = True
                i = 0
                continue
            elif loopstart == -1:
                loopstart = cur
            loop += 1
        else:
            visit[cur] = True
        i += 1
    print(cur + 1)


def __starting_point():
    main()


__starting_point()
