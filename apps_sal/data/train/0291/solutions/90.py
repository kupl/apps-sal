class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        ret = 0
        odd_count, even_count = 0, 0
        
        for num in arr:
            if num % 2 != 0:
                ret += even_count + 1
                odd_count, even_count = even_count + 1, odd_count
            else:
                ret += odd_count
                odd_count, even_count = odd_count, even_count + 1
        
        return ret % (10 ** 9 + 7)
