class Solution:
    def smallestRangeII(self, A: List[int], K: int) -> int:
        if not A:
            return 0
        nums = sorted([num + K for num in set(A)], reverse=True)
        max_num = nums[0]
        min_num = nums[-1]
        changed_max = max_num - 2 * K
        res = max_num - min_num
        for i in range(len(nums) - 1):
            changed = nums[i] - 2 * K
            max_num = max(nums[i + 1], changed, changed_max)
            min_num = min(min_num, changed)
            res = min(res, max_num - min_num)
        return res
