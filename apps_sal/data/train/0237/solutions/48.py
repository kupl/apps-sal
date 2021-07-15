class Solution:
    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        c = collections.Counter({0: 1})
        psum = res = 0
        for i in A:
            psum += i
            res += c[psum - S]
            c[psum] += 1
        return res

                

