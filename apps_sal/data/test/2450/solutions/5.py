import sys

readline = sys.stdin.readline
readlines = sys.stdin.readlines
def ns(): return readline().rstrip()
def ni(): return int(readline().rstrip())
def nm(): return map(int, readline().split())
def nl(): return list(map(int, readline().split()))
def prn(x): return print(*x, sep='\n')


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


T = ni()
for _ in range(T):
    solve()
