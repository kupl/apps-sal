import sys

readline = sys.stdin.readline
read = sys.stdin.read
ns = lambda: readline().rstrip()
ni = lambda: int(readline().rstrip())
nm = lambda: map(int, readline().split())
nl = lambda: list(map(int, readline().split()))
prn = lambda x: print(*x, sep='\n')


def solve():
    n, x, m = nm()
    l = r = x
    for _ in range(m):
        p, q = nm()
        if p <= l <= q:
            l = p
        if p <= r <= q:
            r = q
    print(r - l + 1)
    return


# solve()

T = ni()
for _ in range(T):
    solve()
