import sys

inf = (1 << 31) - 1

def solve():
    n, k = map(int, input().split())

    if k > n - k:
        k = n - k

    s = 0
    res = 1
    a = 1
    ans = [0]*n

    for i in range(n):
        t = (s + k) % n

        if t < s and t > 0:
            res += a + 1
            a += 2
        else:
            res += a

        ans[i] = res

        s = t

    print(*ans)

def __starting_point():
    solve()
__starting_point()
