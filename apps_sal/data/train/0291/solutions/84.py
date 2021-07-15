class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:

        odd = 0
        even = 1
        cnt = 0
        res = 0
        mod = 1000000007
        for i in range(len(arr)):
            if arr[i] % 2 == 1:
                cnt += 1
            if cnt % 2 == 1:
                res = (res + even) % mod
                odd += 1
            else:
                res = (res + odd) % mod
                even += 1
                
        return int(res)
            
            
        

