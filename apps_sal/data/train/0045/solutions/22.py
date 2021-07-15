import sys
ii = lambda: sys.stdin.readline().strip()
idata = lambda: [int(x) for x in ii().split()]

def solve():
    ans = 0
    cnt = 1
    s = 1
    n = int(ii())
    while s <= n:
        cnt = 2 * cnt + 1
        ans += 1
        n -= s
        s = (cnt * (cnt + 1)) // 2
    print(ans)
    return

for t in range(int(ii())):
    solve()

