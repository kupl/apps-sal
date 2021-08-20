class Solution:

    def longestWPI(self, hours: List[int]) -> int:
        hours = [1 if h > 8 else -1 for h in hours]
        down = {1: 0}
        s = 0
        ans = 0
        for (i, h) in enumerate(hours):
            if h < 0:
                if s not in down:
                    down[s] = i
            s += h
            if s in down:
                ans = max(ans, i - down[s])
            if s > 0:
                ans = max(ans, i + 1)
        return ans
