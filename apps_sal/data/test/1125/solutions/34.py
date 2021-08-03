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
    f, s, *a = nm()
    x = 0
    for c in a:
        x ^= c
    if (f + s - x) % 2 or ((f + s - x) // 2) & x:
        print(-1)
        return
    y = (f + s - x) // 2
    for i in range(40, -1, -1):
        if x & (1 << i) and y | (1 << i) <= f:
            y |= 1 << i
    print(f - y if f >= y > 0 else -1)
    return


solve()
