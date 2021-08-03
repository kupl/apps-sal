class Solution:
    def numSubarraysWithSum(self, A: List[int], S: int) -> int:

        d = defaultdict(int)
        d[0] = 1
        psum = res = 0
        for a in A:
            psum += a
            res += d[psum - S]
            d[psum] += 1
        return res
