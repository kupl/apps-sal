class Solution:
    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        ctr = collections.Counter({0: 1})
        prefix = res = 0
        for a in A:
            prefix += a
            res += ctr[prefix - S]
            ctr[prefix] += 1
        return res
