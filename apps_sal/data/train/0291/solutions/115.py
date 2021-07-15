class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        
        even = 0
        odd = 0
        
        res = 0
        for i in range(len(arr)):
            if arr[i] % 2 == 1:
                odd, even = even + 1, odd
                res += odd
            else:
                even += 1
                res += odd
        
        return res % 1000000007
