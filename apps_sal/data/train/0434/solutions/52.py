class Solution:

    def longestSubarray(self, nums: List[int]) -> int:
        seq = [0]
        prev = 0
        res = 0
        for n in nums:
            if n:
                seq[-1] += 1
                res = max(prev + seq[-1], res)
            else:
                prev = seq[-1]
                seq.append(0)
        if len(seq) == 1:
            res -= 1
        return res
