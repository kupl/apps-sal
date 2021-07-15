class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        if len(arr) <= 1:
            return 0
        
        p1 = 0
        p2 = len(arr) - 1
        
        for i in range(1,len(arr)):
            if arr[i] >= arr[i-1]:
                p1 += 1
            else:
                break
        
        for i in range(len(arr)-2, -1, -1):
            if arr[i] <= arr[i+1]:
                p2 = i
            else:
                break
        ans = min(len(arr) - p1 - 1 , p2)
        if p1 > p2:
             return ans
        p11, p22 = 0, p2
        
        while p11 <= p1 and p22 < len(arr):
            if arr[p11] <= arr[p22]:
                ans = min(ans, p22 - p11 - 1)
                p11 += 1
            else:
                p22 += 1
        return ans
