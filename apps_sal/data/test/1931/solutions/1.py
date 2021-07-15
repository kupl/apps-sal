import sys

readline = sys.stdin.readline

ns = lambda: readline().rstrip()
ni = lambda: int(readline().rstrip())
nm = lambda: list(map(int, readline().split()))
nl = lambda: list(map(int, readline().split()))

def solve():
    n = ni()
    ans = 0
    while n > 1:
        ok, ng = 0, 10**5
        while ng - ok > 1:
            mid = (ok + ng) // 2
            if mid*(mid+1)*3//2 - mid <= n:
                ok = mid
            else:
                ng = mid
        n -= ok*(ok+1)*3//2 - ok
        ans += 1
    print(ans)


# solve()

T = ni()
for _ in range(T):
    solve()

