import sys

readline = sys.stdin.readline
read = sys.stdin.read
ns = lambda: readline().rstrip()
ni = lambda: int(readline().rstrip())
nm = lambda: map(int, readline().split())
nl = lambda: list(map(int, readline().split()))
prn = lambda x: print(*x, sep='\n')


def solve():
    s = list(map(lambda x: int(x) - 1, list(ns())))
    n = len(s)
    l = [3 * n] * 3
    ans = 3 * n
    for i in range(n - 1, -1, -1):
        l[s[i]] = i
        ans = min(ans, max(l) - i + 1)
    print(ans if ans <= n else 0)
    return


# solve()

T = ni()
for _ in range(T):
    solve()
