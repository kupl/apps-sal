class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ans = 0
        N = len(nums)

        allzeros = False
        while not allzeros:
            allzeros = True
            for i in range(N):
                if nums[i] % 2 > 0:
                    ans += 1
                    nums[i] -= 1
                if nums[i] != 0:
                    allzeros = False
                    nums[i] = nums[i] // 2

            if not allzeros:
                ans += 1
            # print(ans, nums)

        return ans
