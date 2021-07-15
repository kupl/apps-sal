class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        left = [float('inf') for _ in range(len(arr))]
        right = [-float('inf') for _ in range(len(arr))]
        
        last = -float('inf')
        for i,x in enumerate(arr):
            if x >= last:
                left[i] = x
            else:
                break
            last = x
        last = float('inf')
        _n = len(arr) - 1
        right_k = 0
        for i,x in enumerate(reversed(arr)):
            if x <= last:
                right[_n-i] = x
            else:
                right_k = i
                break
            last = x
            
        ans = float('inf')
        import bisect
        for i,x in enumerate(left):
            if x < float('inf'):
                j = bisect.bisect_left(right, x, i+1)
                ans = min(ans, j-i-1)
            else:
                break
        ans = min(ans, len(arr)-right_k)
        return ans
