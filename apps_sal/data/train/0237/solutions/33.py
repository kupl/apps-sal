class Solution:
    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        A = [0] + list(itertools.accumulate(A))
        hm = Counter()
        res = 0
        for i in A:
            res += hm[i]
            hm[i+S] += 1
        return res
