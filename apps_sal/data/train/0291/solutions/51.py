class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        # keep array that holds # of even/odd sum subarrays that end at that index
        ans = odd = even = 0
        for i in range(len(arr)):
            if arr[i] % 2 == 0: # even
                even = even + 1
                ans += odd
            else:               # odd
                even, odd = odd, even + 1
                ans += odd
                
        return ans % (10**9 + 7)
