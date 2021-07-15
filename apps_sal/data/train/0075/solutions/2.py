import sys
import math

readline = sys.stdin.readline
read = sys.stdin.read
ns = lambda: readline().rstrip()
ni = lambda: int(readline().rstrip())
nm = lambda: map(int, readline().split())
nl = lambda: list(map(int, readline().split()))
prn = lambda x: print(*x, sep='\n')


def solve():
    n = ni()
    print(math.cos(math.pi / (4 * n)) / math.sin(math.pi / (2 * n)))
    return


# solve()

T = ni()
for _ in range(T):
    solve()

