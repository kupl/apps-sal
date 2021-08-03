import sys

readline = sys.stdin.readline
readlines = sys.stdin.readlines
def ns(): return readline().rstrip()
def ni(): return int(readline().rstrip())
def nm(): return map(int, readline().split())
def nl(): return list(map(int, readline().split()))
def prn(x): return print(*x, sep='\n')


def solve():
    n = ni()
    s = nl()
    dp = [1] * (n + 1)
    for i in range(n // 2, 0, -1):
        for j in range(2 * i, n + 1, i):
            if s[i - 1] < s[j - 1]:
                dp[i] = max(dp[i], dp[j] + 1)

    print(max(dp))
    return

# solve()


T = ni()
for _ in range(T):
    solve()
