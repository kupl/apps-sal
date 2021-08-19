class Solution:

    def longestWPI(self, hours: List[int]) -> int:
        n = len(hours)
        hours = [1 if x > 8 else -1 for x in hours]
        s = 0
        idx = {}
        ans = 0
        for i in range(len(hours)):
            s += hours[i]
            if s > 0:
                ans = i + 1
            if s not in idx:
                idx[s] = i
            if s - 1 in idx:
                ans = max(ans, i - idx[s - 1])
        return ans
