class Solution:
    def minOperations(self, nums: List[int]) -> int:
        def check(nums):
            flag = False
            for n in nums:
                if n > 1:
                    flag = True
            return flag

        cnt = 0
        n = len(nums)
        flag = check(nums)
        while flag:
            # print(nums)
            cnt += 1
            for i in range(n):
                if nums[i] % 2:
                    nums[i] -= 1
                    nums[i] = nums[i] // 2
                    cnt += 1
                else:
                    nums[i] = nums[i] // 2
            # print(cnt)
            flag = check(nums)
        for n in nums:
            if n != 0:
                cnt += 1
        return cnt
