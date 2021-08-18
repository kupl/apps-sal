from collections import Counter

'''
let P[i] = sum(A[:i])
for each j
    count 
        where P[j] - P[i] = S where i < j
'''


class Solution:
    def numSubarraysWithSum(self, A, k):
        count = Counter({0: 1})
        ans = psum = 0

        for v in A:
            psum += v
            ans += count[psum - k]
            count[psum] += 1

        return ans
