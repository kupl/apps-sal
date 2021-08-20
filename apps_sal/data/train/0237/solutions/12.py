from collections import Counter
"\nlet P[i] = sum(A[:i])\nfor each j\n    count # of i's \n        where P[j] - P[i] = S where i < j\n"


class Solution:

    def numSubarraysWithSum(self, A, k):
        count = Counter({0: 1})
        ans = psum = 0
        for v in A:
            psum += v
            ans += count[psum - k]
            count[psum] += 1
        return ans
