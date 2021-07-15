class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        SUM = 0
        MIN = 0
        minsum = sys.maxsize
        MAX = 0
        maxsum = -sys.maxsize
        
        for num in A:
            SUM += num
            maxsum = max(maxsum, SUM-MIN)
            MIN = min(MIN,SUM)
            minsum = min(minsum, SUM-MAX)
            MAX = max(MAX,SUM)
        if minsum == SUM:
            return maxsum
        return max(maxsum, SUM-minsum)
