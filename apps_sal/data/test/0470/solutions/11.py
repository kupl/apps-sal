from collections import Counter


def solve():
    N = list(map(int, input().split()))
    S = sum(N)
    co = Counter(N)
    ans = S
    for n in co:
        if co[n] >= 3:
            ans = min(ans, S - n * 3)
        elif co[n] == 2:
            ans = min(ans, S - n * 2)
    print(ans)


def __starting_point():
    solve()


__starting_point()
