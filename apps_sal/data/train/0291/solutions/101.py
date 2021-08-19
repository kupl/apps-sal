class Solution:

    def numOfSubarrays(self, arr: List[int]) -> int:
        count = len(arr)
        pre_odd_count = arr[0] % 2
        pre_even_count = 1 - pre_odd_count
        result = pre_odd_count
        for index in range(1, count):
            isodd = arr[index] % 2
            if isodd:
                temp = pre_odd_count
                pre_odd_count = 1 + pre_even_count
                pre_even_count = temp
            else:
                pre_odd_count = pre_odd_count
                pre_even_count = 1 + pre_even_count
            result += pre_odd_count
        return result % 1000000007
