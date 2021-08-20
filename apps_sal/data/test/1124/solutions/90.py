from math import gcd


def solve():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        ans = gcd(ans, A[i])
    print(ans)


def __starting_point():
    solve()


__starting_point()
