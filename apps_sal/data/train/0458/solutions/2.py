class Solution:

    def minSubarray(self, nums: List[int], p: int) -> int:
        remain = sum(nums) % p
        if remain == 0:
            return 0
        dic = {0: -1}
        (presum, res) = (0, float('inf'))
        for (i, num) in enumerate(nums):
            presum += num
            cur_remain = presum % p
            dic[cur_remain] = i
            target = (cur_remain - remain) % p
            if target in dic:
                res = min(res, i - dic[target])
        return res if res < len(nums) else -1
