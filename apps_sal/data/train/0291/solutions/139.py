class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        limit = 10**9 + 7

        final = 0
        dp_even = [0] * (len(arr) + 1)
        dp_odd = [0] * (len(arr) + 1)
        for i in range(len(arr)):
            num = arr[i]
            if num % 2 == 0:
                odd_cur = dp_odd[i]
                even_cur = 1 + dp_even[i]
                final += odd_cur
                dp_even[i + 1] = even_cur
                dp_odd[i + 1] = odd_cur
            else:
                odd_cur = dp_even[i] + 1
                even_cur = dp_odd[i]
                final += odd_cur
                dp_odd[i + 1] = odd_cur
                dp_even[i + 1] = even_cur

        return final % limit
