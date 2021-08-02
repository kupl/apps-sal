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
    l = [1] * (k - 1) + [n - k + 1]
    if l[-1] > 0 and l[-1] % 2:
        print('YES')
        print(*l)
        return
    l = [2] * (k - 1) + [n - 2 * (k - 1)]
    if l[-1] > 0 and l[-1] % 2 == 0:
        print('YES')
        print(*l)
        return
    print('NO')
    return

# solve()


T = ni()
for _ in range(T):
    solve()
