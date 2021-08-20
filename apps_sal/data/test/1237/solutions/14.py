def solve():
    (N, S) = list(map(int, input().split()))
    PS = []
    for i in range(N):
        (f, t) = list(map(int, input().split()))
        PS.append((f, t))
    PS.sort(key=lambda p: -p[0])
    ans = 0
    for (f, t) in PS:
        ans += S - f
        S = f
        if ans < t:
            ans = t
    if S != 0:
        ans += S
    print(ans)


def __starting_point():
    solve()


__starting_point()
