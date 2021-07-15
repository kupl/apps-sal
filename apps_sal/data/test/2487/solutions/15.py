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
    a = n * (n + 1) * (n + 2) // 6
    for i in range(n-1):
        u, v = nm()
        if u > v:
            u, v = v, u
        a -= u * (n - v + 1)
    print(a)
    return

solve()

