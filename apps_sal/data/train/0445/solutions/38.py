import heapq

class Solution:
    def minDifference(self, nums: List[int]) -> int:
        largest = heapq.nlargest(4, nums)
        smallest = heapq.nsmallest(4, nums)
        
        m = 10**10
        n = len(largest)
        for i in range(n):
            m = min(m, largest[i] - smallest[n - 1 -i])
        return max(m, 0)
