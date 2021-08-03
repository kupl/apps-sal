class Solution:
    def longestSubarray(self, a: List[int]) -> int:
        ones = 0
        old_ones = 0
        maxlen = 0
        n = len(a)
        for i in range(n):
            if a[i] == 1:
                ones += 1
                maxlen = max(maxlen, ones + old_ones)
            else:
                old_ones = ones
                ones = 0

        return maxlen if ones < n else n - 1
