import sys

readline = sys.stdin.readline
readlines = sys.stdin.readlines
ns = lambda: readline().rstrip()
ni = lambda: int(readline().rstrip())
nm = lambda: map(int, readline().split())
nl = lambda: list(map(int, readline().split()))
prn = lambda x: print(*x, sep='\n')


def solve():
    n, k = nm()
    for i in range(2, n+1):
        if n % i == 0:
            n += i
            break
    n += 2 * (k-1)
    print(n)
    return

# solve()

T = ni()
for _ in range(T):
    solve()

