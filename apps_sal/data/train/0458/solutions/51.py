class Solution:

    def minSubarray(self, nums: List[int], p: int) -> int:
        n = result = len(nums)
        need = cur = 0
        for num in nums:
            need = (need + num) % p
        last = collections.defaultdict(lambda: -n)
        last[0] = -1
        for (i, num) in enumerate(nums):
            cur = (cur + num) % p
            last[cur] = i
            want = (p - need + cur) % p
            result = min(result, i - last[want])
        return result if result < n else -1
