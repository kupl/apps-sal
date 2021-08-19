class Solution:

    def longestOnes(self, A: List[int], K: int) -> int:
        left = 0
        maxLen = 0
        oneFreq = 0
        maxFreq = 0
        for right in range(len(A)):
            oneFreq += A[right]
            maxFreq = max(maxFreq, oneFreq)
            if right - left + 1 - maxFreq > K:
                oneFreq -= A[left]
                left += 1
            maxLen = max(maxLen, right - left + 1)
        return maxLen
