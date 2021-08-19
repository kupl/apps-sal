"""input
8
20 1000
32 37
40 1000
45 50
16 16
16 16
14 1000
2 1000
"""
import heapq
from bisect import bisect
inf = 10 ** 18 + 2


def rints():
    return list(map(int, input().split()))


def ri():
    return int(input())


def bin_search(arr, pred, lo=0, hi=None):
    if hi is None:
        hi = len(arr)
    while lo < hi:
        mid = (lo + hi) // 2
        if pred(arr[mid]):
            hi = mid
        else:
            lo = mid + 1
    return lo


n = ri()
(score, _) = rints()
teams = []
for _ in range(n - 1):
    (t, w) = rints()
    teams.append((w - t + 1, t, w))
teams.sort(key=lambda x: x[1])


def solve(score):
    idx = bin_search(teams, lambda x: x[1] > score)
    best = pos = len(teams) - idx + 1
    ahead = teams[idx:]
    behind = teams[:idx]
    heapq.heapify(ahead)
    while ahead and score >= ahead[0][0]:
        score -= heapq.heappop(ahead)[0]
        pos -= 1
        while behind and behind[-1][1] > score:
            heapq.heappush(ahead, behind.pop())
            pos += 1
        best = min(best, pos)
    return best


print(solve(score))
