import sys
input = sys.stdin.readline

def solve():
    INF = float('inf')

    def min2(x, y): return x if x <= y else y

    H, N = list(map(int, input().split()))
    items = [tuple(map(int, input().split())) for _ in range(N)]

    items.sort()

    dp = [INF] * (H+1)
    dp[0] = 0
    for vi, wi in items:
        for j in range(H-vi+1):
            dp[j+vi] = min2(dp[j+vi], dp[j]+wi)
        for j in range(max(0, H-vi+1), H+1):
            dp[H] = min2(dp[H], dp[j]+wi)
#        print(dp)

    print((dp[H]))


solve()

