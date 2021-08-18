class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        need = sum(nums) % p
        cumsum = 0
        last = collections.defaultdict(lambda: -math.inf)
        last[0] = -1
        result = math.inf
        for ind, val in enumerate(nums):
            cumsum += val
            last[cumsum % p] = ind
            result = min(result, ind - last[(cumsum - need) % p])
        if result == math.inf or result == len(nums):
            return -1
        else:
            return result
