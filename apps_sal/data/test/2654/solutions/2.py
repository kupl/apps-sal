
def solve():
    N = int(input())
    Ls, Rs = [], []
    for i in range(N):
        a, b = list(map(int, input().split()))
        Ls.append(a), Rs.append(b)
    Ls.sort(), Rs.sort()

    ans = 0
    if N % 2 == 1:
        l = Ls[N // 2]
        r = Rs[N // 2]
        ans = r - l + 1
    else:
        l2 = Ls[N // 2 - 1] + Ls[N // 2]
        r2 = Rs[N // 2 - 1] + Rs[N // 2]
        ans = r2 - l2 + 1

    print(ans)


def __starting_point():
    solve()


__starting_point()
