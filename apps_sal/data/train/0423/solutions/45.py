class Solution:

    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        mem = collections.defaultdict(int)
        res = 0
        for n in arr:
            if mem[n - difference] + 1 > mem[n]:
                mem[n] = mem[n - difference] + 1
            res = max(res, mem[n])
        return res
