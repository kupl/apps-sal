class Solution:

    def numOfSubarrays(self, arr: List[int]) -> int:
        sum_even = 0
        sum_odd = 0
        out = 0
        for i in range(len(arr)):
            if arr[i] % 2 == 0:
                (sum_even, sum_odd) = (sum_even + 1, sum_odd)
            else:
                (sum_even, sum_odd) = (sum_odd, sum_even + 1)
            out = out + sum_odd
        return out % 1000000007
