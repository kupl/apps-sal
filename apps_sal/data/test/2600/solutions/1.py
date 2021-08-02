import sys

readline = sys.stdin.readline
read = sys.stdin.read
ns = lambda: readline().rstrip()
ni = lambda: int(readline().rstrip())
nm = lambda: map(int, readline().split())
nl = lambda: list(map(int, readline().split()))
prn = lambda x: print(*x, sep='\n')


def solve():
    h, w = nm()
    a = [nl() for _ in range(h)]
    d = dict()
    for i in range(h):
        for j in range(w):
            v = min(i + j, h + w - 2 - i - j)
            if v not in d:
                d[v] = [0, 0]
            d[v][a[i][j]] += 1
    ans = 0
    for x in d:
        if x * 2 != h + w - 2:
            ans += min(d[x])
    print(ans)
    return


# solve()

T = ni()
for _ in range(T):
    solve()
