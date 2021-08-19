import sys
mod = 10 ** 9 + 7


def solve():
    n = int(input())
    x = [int(i) for i in input().split()]
    x.sort()
    ans = 0
    p2 = [1] * (n + 1)
    for i in range(n):
        p2[i + 1] = p2[i] * 2 % mod
    for i in range(n - 1):
        length = x[i + 1] - x[i]
        ans = (ans + length * (p2[i + 1] - 1) * (p2[n - 1 - i] - 1)) % mod
    print(ans)


def __starting_point():
    solve()


__starting_point()
