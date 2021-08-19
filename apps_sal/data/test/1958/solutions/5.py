def solve():
    (N, P) = list(map(int, input().split()))
    m = []
    for i in range(N):
        s = input()
        m.append(s)
    m.reverse()
    cur = 0
    ans = 0
    for s in m:
        if s == 'halfplus':
            nex = cur * 2 + 1
        else:
            nex = cur * 2
        ans += nex * P // 2
        cur = nex
    print(ans)


def __starting_point():
    solve()


__starting_point()
