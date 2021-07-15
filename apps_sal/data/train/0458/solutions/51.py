class Solution:
    # def minSubarray(self, nums: List[int], p: int) -> int:
    #     n = len(nums)
    #     sumArr = [0] * (n + 1)
    #     for i in range(1, n + 1):
    #         sumArr[i] = nums[i - 1] + sumArr[i - 1]
    #     if sumArr[n] % p == 0:
    #         return 0
    #     remove = 1
    #     while remove < n:
    #         for i in range(remove, n + 1):
    #             total = sumArr[n] - (sumArr[i] - sumArr[i - remove])
    #             if total % p == 0:
    #                 return remove
    #         remove += 1
    #     return -1
    
    def minSubarray(self, nums: List[int], p: int) -> int:
        n = result = len(nums)
        need = cur = 0
        for num in nums:
            need = (need + num) % p
        last = collections.defaultdict(lambda: -n)
        last[0] = -1
        for i, num in enumerate(nums):
            cur = (cur + num) % p
            last[cur] = i
            want = (p - need + cur) % p
            result = min(result, i - last[want])
        return result if result < n else -1

