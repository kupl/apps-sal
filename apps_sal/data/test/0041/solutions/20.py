import sys

inf = 1 << 30

def solve():
    n = int(input())
    a = [int(i) for i in input().split()]

    ans = [inf]*n

    d = inf

    for i in range(n):
        if a[i] == 0:
            d = 0

        ans[i] = d
        d += 1

    d = inf

    for i in reversed(range(n)):
        if a[i] == 0:
            d = 0

        ans[i] = min(ans[i], d)
        d += 1

    print(*ans)

def __starting_point():
    solve()
__starting_point()
