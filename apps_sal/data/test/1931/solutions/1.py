import sys

readline = sys.stdin.readline


def ns(): return readline().rstrip()
def ni(): return int(readline().rstrip())
def nm(): return list(map(int, readline().split()))
def nl(): return list(map(int, readline().split()))


def solve():
    n = ni()
    ans = 0
    while n > 1:
        ok, ng = 0, 10**5
        while ng - ok > 1:
            mid = (ok + ng) // 2
            if mid * (mid + 1) * 3 // 2 - mid <= n:
                ok = mid
            else:
                ng = mid
        n -= ok * (ok + 1) * 3 // 2 - ok
        ans += 1
    print(ans)


# solve()

T = ni()
for _ in range(T):
    solve()
