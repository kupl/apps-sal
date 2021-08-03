class Solution:
    def minOperations(self, nums: List[int]) -> int:
        cnt = 0
        while any(nums):
            even = 0
            # if any odd -> deduct 1 from all
            for k, v in enumerate(nums):
                if v % 2 == 1:
                    cnt += 1
                    nums[k] -= 1
                elif v > 0:
                    even += 1
            if even > 0:
                nums = list([x // 2 for x in nums])
                cnt += 1

        return cnt
