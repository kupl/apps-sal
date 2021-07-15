class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        ans = 0
        odd = 0
        even = 0
        tot = 0
        for i in range(len(arr)):
            tot += arr[i]
            if tot%2==0:
                even +=1
            else:
                odd += 1
            
            if tot%2!=0:
                ans +=1
                ans += even
            else:
                ans += odd
        
        return ans % (10**9 + 7)
