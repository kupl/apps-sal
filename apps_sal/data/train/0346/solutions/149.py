from collections import Counter


class Solution:

    def numberOfSubarrays(self, A, k):
        psum = [0]
        for x in map(lambda x: x % 2, A):
            psum.append(psum[-1] + x)
        count = Counter(psum)
        return sum((count[p - k] for p in psum))
