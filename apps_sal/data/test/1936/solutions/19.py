import sys

readline = sys.stdin.readline
readlines = sys.stdin.readlines
ns = lambda: readline().rstrip()
ni = lambda: int(readline().rstrip())
nm = lambda: map(int, readline().split())
nl = lambda: list(map(int, readline().split()))
prn = lambda x: print(*x, sep='\n')


def solve():
    a, b = nm()
    if a * 2 > b:
        print(-1, -1)
    else:
        print(a, 2*a)
    return


# solve()

T = ni()
for _ in range(T):
    solve()

