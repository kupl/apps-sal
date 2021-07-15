import sys

readline = sys.stdin.readline
readlines = sys.stdin.readlines
ns = lambda: readline().rstrip()
ni = lambda: int(readline().rstrip())
nm = lambda: map(int, readline().split())
nl = lambda: list(map(int, readline().split()))
prn = lambda x: print(*x, sep='\n')

def solve():
    n, m, k = nm()
    if n // k >= m:
        print(m)
        return
    else:
        m -= n // k
        print(n // k - (m-1)//(k-1) - 1)
    return


# solve()

T = ni()
for _ in range(T):
    solve()

