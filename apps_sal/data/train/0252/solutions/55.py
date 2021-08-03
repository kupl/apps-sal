class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        ls = []
        for i in range(n + 1):
            ls.append((max(i - ranges[i], 0), min(i + ranges[i], n + 1)))
        ls.sort(key=lambda x: (x[0], -x[1]))
        ans, a, b = 0, -1, 0
        while b < n:
            c, d = ls.pop(0)
            if c > b:
                return -1
            elif d <= b:
                continue
            elif c > a:
                ans += 1
                a, b = b, d
            elif c <= a:
                b = d
        return ans
