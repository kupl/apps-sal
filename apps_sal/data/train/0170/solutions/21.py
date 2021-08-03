class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)
        if(n == 1):
            return 0
        l = 0
        r = n - 1
        while(r > 0):
            if(arr[r - 1] > arr[r]):
                break
            r = r - 1
        ans = r - l
        while(l < r):
            if(l > 0 and arr[l - 1] > arr[l]):
                break
            while(r < n and arr[r] < arr[l]):
                r = r + 1
            ans = min(ans, r - l - 1)
            l = l + 1
        return ans
