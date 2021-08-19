class Solution:

    def minTaps(self, n: int, ranges: List[int]) -> int:
        (furthest, cnt, cur) = ([0] * n, 0, 0)
        for i in range(n + 1):
            l = max(0, i - ranges[i])
            r = min(n, i + ranges[i])
            for j in range(l, r):
                furthest[j] = max(furthest[j], r)
        while cur < n:
            if furthest[cur] == 0:
                return -1
            cur = furthest[cur]
            cnt += 1
        return cnt
