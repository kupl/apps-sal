class Solution:

    def minOperations(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        not_zero = set(list(range(n)))
        while True:
            if len(not_zero) == 0:
                return ans
            zeros = []
            for i in not_zero:
                if nums[i] % 2 == 1:
                    nums[i] -= 1
                    ans += 1
                if nums[i] == 0:
                    zeros.append(i)
                nums[i] = nums[i] // 2
            for j in zeros:
                not_zero.remove(j)
            if len(not_zero) > 0:
                ans += 1
