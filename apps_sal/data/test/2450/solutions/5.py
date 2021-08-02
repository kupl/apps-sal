import sys

readline = sys.stdin.readline
readlines = sys.stdin.readlines
ns = lambda: readline().rstrip()
ni = lambda: int(readline().rstrip())
nm = lambda: map(int, readline().split())
nl = lambda: list(map(int, readline().split()))
prn = lambda x: print(*x, sep='\n')


def solve():
    n, m, x, y = nm()
    y = min(y, 2 * x)
    ans = 0
    for _ in range(n):
        s = ns().split('*')
        for f in s:
            ans += len(f) // 2 * y + len(f) % 2 * x
    print(ans)
    return


# solve()

T = ni()
for _ in range(T):
    solve()
