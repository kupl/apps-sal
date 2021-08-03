class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        i = j = maxCount = maxlen = 0
        d = {0: 0, 1: 0}
        while(i < len(A)):
            d[A[i]] += 1
            while(d[0] > K):
                d[A[j]] -= 1
                j += 1
            maxlen = max(maxlen, i - j + 1)
            i += 1
        return maxlen
