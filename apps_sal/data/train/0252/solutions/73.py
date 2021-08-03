class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        # max_right from each point
        max_right = [0] * (n + 1)
        for i, x in enumerate(ranges):
            l = max(0, i - x)
            r = min(n, i + x)
            max_right[l] = r
        # jump game
        ans = 0
        reach = 0
        while reach < n:
            max_reach = max(r for r in max_right[:reach + 1])
            if max_reach <= reach:
                return -1
            reach = max_reach
            ans += 1
        return ans
