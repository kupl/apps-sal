from collections import Counter


class Solution:
    def numberOfSubarrays(self, A, k):
        count = Counter([0])

        ans = 0
        psum = 0
        for v in A:
            psum += v % 2
            ans += count[psum - k]
            count[psum] += 1

        return ans
