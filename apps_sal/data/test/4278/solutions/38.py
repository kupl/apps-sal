def solve(N, Ss):
    for i in range(N):
        Ss[i] = ''.join(sorted(list(Ss[i])))
    Ss.sort()
    ans = 0
    flg = False
    counter = 0
    for i in range(N - 1):
        if Ss[i] == Ss[i + 1]:
            if not flg:
                flg = True
                counter = i
        elif flg:
            ans += (i - counter + 1) * (i - counter) // 2
            flg = False
    if flg:
        ans += (N - 1 - counter + 1) * (N - 1 - counter) // 2
    print(ans)


def __starting_point():
    N = int(input())
    Ss = [input() for _ in range(N)]
    solve(N, Ss)


__starting_point()
