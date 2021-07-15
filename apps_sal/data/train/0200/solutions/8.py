class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        
        if k == 0:
            return 0
        
        a,b = 1, 1
        while b <= k:
            a,b = b, a+b
        return self.findMinFibonacciNumbers(k-a)+1
        
        
#         arr = [1, 1]
#         while arr[-1] <= k:
#             arr.append( arr[-1]+arr[-2] )   # O(n) space
        
#         d = k-arr[-2]
        
#         cnt = 1
        
#         while d > 0:
#             ind = bisect.bisect_right(arr, d)  # O(n log n) 
#             d -= arr[ind-1]
#             cnt += 1
        
#         return cnt
        

