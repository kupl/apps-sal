import math
from collections import defaultdict


def main():
    n, k = list(map(int, input().split()))
    cards = list(map(int, input().split()))
    fav = list(map(int, input().split()))

    h = [0] + list(map(int, input().split()))

    cards_cnt = defaultdict(int)
    for val in cards:
        cards_cnt[val] += 1

    players_fav_cnt = defaultdict(int)
    for val in fav:
        players_fav_cnt[val] += 1

    # dp[a][b] - a players, b favourite cards (in total)
    dp = [[0 for _ in range(k*n+k+1)] for _ in range(n+1)]
    for p in range(n):
        for c in range(k*n+1):
            for hand in range(k+1):
                dp[p+1][c+hand] = max(dp[p+1][c+hand], dp[p][c] + h[hand])

    res = 0
    for f in players_fav_cnt:
        res += dp[players_fav_cnt[f]][cards_cnt[f]]

    print(res)


def __starting_point():
    main()

__starting_point()
