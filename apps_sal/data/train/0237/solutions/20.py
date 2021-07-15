class Solution:
    def numSubarraysWithSum(self, A, S):
        c = collections.Counter({0: 1})
        psum = res = 0
        for i in A:
            psum += i
            res += c[psum - S]
            c[psum] += 1
        return res
