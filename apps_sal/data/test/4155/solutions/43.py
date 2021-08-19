def solve(N, hi):
    ans = 0
    for i in range(max(hi)):
        flg = False
        for n in range(N):
            if hi[n] != 0:
                if not flg:
                    flg = True
                    ans += 1
                hi[n] -= 1
            else:
                flg = False
    print(ans)


def __starting_point():
    N = int(input())
    hi = [int(i) for i in input().split()]
    solve(N, hi)


__starting_point()
