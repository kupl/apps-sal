class Solution:

    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        count = Counter(arr)
        if difference == 0:
            return max(count.values())
        n = len(arr)
        dd = dict()
        ans = 1
        for (i, n) in enumerate(arr):
            if n - difference in dd:
                dd[n] = 1 + dd[n - difference]
            else:
                dd[n] = 1
            ans = max(ans, dd[n])
        return ans
