import sys

readline = sys.stdin.readline
read = sys.stdin.read
def ns(): return readline().rstrip()
def ni(): return int(readline().rstrip())
def nm(): return map(int, readline().split())
def nl(): return list(map(int, readline().split()))
def prn(x): return print(*x, sep='\n')


def solve():
    a, b, c, d = nm()
    if a <= b:
        print(b)
    else:
        a -= b
        if c <= d:
            print(-1)
        else:
            print(b + c * ((a - 1) // (c - d) + 1))
    return


# solve()

T = ni()
for _ in range(T):
    solve()
