class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        need = sum(nums) % p
        memo = {0: -1}
        prefix = 0
        min_len = n = len(nums)
        
        for idx, num in enumerate(nums):
            prefix = (prefix + num) % p
            memo[prefix] = idx
            if (prefix - need) % p in memo:
                min_len = min(min_len, idx - memo[(prefix - need) % p])
        return min_len if min_len != n else -1
                

