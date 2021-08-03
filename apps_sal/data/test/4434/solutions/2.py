import sys

readline = sys.stdin.readline
readall = sys.stdin.read
def ns(): return readline().rstrip()
def ni(): return int(readline().rstrip())
def nm(): return map(int, readline().split())
def nl(): return list(map(int, readline().split()))
def prn(x): return print(*x, sep='\n')


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
