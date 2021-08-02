import sys

readline = sys.stdin.readline
readall = sys.stdin.read
ns = lambda: readline().rstrip()
ni = lambda: int(readline().rstrip())
nm = lambda: map(int, readline().split())
nl = lambda: list(map(int, readline().split()))
prn = lambda x: print(*x, sep='\n')


def solve():
    n = ni()
    c = 0
    for i in range(n // 2):
        c += (i + 1) * (i + 1) * 2 * 4
    print(c)
    return

# solve()


T = ni()
for _ in range(T):
    solve()
