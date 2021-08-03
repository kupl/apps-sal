class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        record = collections.defaultdict(int)
        res = 0
        for i, v in enumerate(arr):
            l = 1
            if v - difference in record:
                l = record[v - difference] + 1
            record[v] = l
            res = max(res, l)
        return res
