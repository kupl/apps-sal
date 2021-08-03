import sys
import math

readline = sys.stdin.readline
read = sys.stdin.read
def ns(): return readline().rstrip()
def ni(): return int(readline().rstrip())
def nm(): return map(int, readline().split())
def nl(): return list(map(int, readline().split()))
def prn(x): return print(*x, sep='\n')


def solve():
    n = ni()
    print(math.cos(math.pi / (4 * n)) / math.sin(math.pi / (2 * n)))
    return


# solve()

T = ni()
for _ in range(T):
    solve()
