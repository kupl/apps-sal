import sys

readline = sys.stdin.readline
readlines = sys.stdin.readlines
ns = lambda: readline().rstrip()
ni = lambda: int(readline().rstrip())
nm = lambda: map(int, readline().split())
nl = lambda: list(map(int, readline().split()))
prn = lambda x: print(*x, sep='\n')


def solve():
    n, k = nm()
    a, b = nm()
    c, d = nm()
    if d < b:
        a, b, c, d = c, d, a, b
    if a <= c <= b:
        cur = (b - c) * n
        if (d - a) * n > k:
            print(max(k - cur, 0))
        else:
            ans = (d - a) * n - cur
            print(ans + (k - (d - a) * n) * 2)
    elif c < a:
        cur = (b - a) * n
        if (d - c) * n > k:
            print(max(k - cur, 0))
        else:
            ans = (d - c) * n - cur
            print(ans + (k - (d - c) * n) * 2)
    else:
        ans = 10**18
        cur = 0
        for i in range(n):
            cur += c - b
            if k > d - a:
                k -= d - a
                cur += d - a
            else:
                cur += k
                k -= k
            ans = min(ans, cur + k * 2)
        print(ans)
    return


# solve()

T = ni()
for _ in range(T):
    solve()
