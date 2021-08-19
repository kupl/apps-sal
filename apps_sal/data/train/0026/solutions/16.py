import sys

readline = sys.stdin.readline


def ns(): return readline().rstrip()
def ni(): return int(readline().rstrip())
def nm(): return list(map(int, readline().split()))
def nl(): return list(map(int, readline().split()))


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
