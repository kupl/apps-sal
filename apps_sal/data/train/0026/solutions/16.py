import sys

readline = sys.stdin.readline

ns = lambda: readline().rstrip()
ni = lambda: int(readline().rstrip())
nm = lambda: list(map(int, readline().split()))
nl = lambda: list(map(int, readline().split()))

def solve():
    n, m = nm()
    if min(n, m) == 1 or max(n, m) == 2:
        print('YES')
    else:
        print('NO')

# solve()

T = ni()
for _ in range(T):
    solve()

