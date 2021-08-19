class Solution:

    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        d = {}
        for a in arr:
            a_ = a - difference
            if difference == 0:
                if a not in d:
                    d[a] = 1
                else:
                    d[a] = d[a] + 1
            else:
                if a not in d:
                    d[a] = 1
                if a - difference in d:
                    d[a] = max(d[a], d[a - difference] + 1)
        return max(d.values())
