class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        limit = 10**9 + 7
        # use dp:
        
        # the number of odd sums ending at each index
        final = 0 
        dp_even = [0] * (len(arr ) + 1)
        dp_odd = [0] * (len(arr ) + 1)
        for i in range(len(arr)):
            num = arr[i]
            if num%2 == 0:
                # if this number is even, so we need to find the count of prev odd
                odd_cur = dp_odd[i]
                even_cur = 1 + dp_even[i]
                final += odd_cur
                dp_even[i + 1] = even_cur
                dp_odd[i + 1] = odd_cur
                # so we need to calculate the number odd and even sum ending at each index
            else:
                odd_cur = dp_even[i] + 1
                even_cur = dp_odd[i]
                final += odd_cur
                dp_odd[i + 1] = odd_cur
                dp_even[i + 1] = even_cur
                
        return final % limit
