class Solution:

    def numOfSubarrays(self, arr: List[int]) -> int:
        mod = 10 ** 9 + 7
        odd_presum_cnt = 0
        par = 0
        for a in arr:
            par ^= a & 1
            if par:
                odd_presum_cnt += 1
        return odd_presum_cnt * (len(arr) + 1 - odd_presum_cnt) % mod
