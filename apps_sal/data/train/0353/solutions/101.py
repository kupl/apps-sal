class Solution:

    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        j = len(nums) - 1
        flag = False
        ans = 0
        for i in range(len(nums)):
            if flag:
                if nums[i] * 2 > target:
                    break
                ans += 1
            else:
                while j >= i and nums[j] + nums[i] > target:
                    j -= 1
                if j > i:
                    ans += 2 ** (j - i)
                else:
                    if nums[i] * 2 > target:
                        break
                    ans += 1
                    flag = True
        return ans % (10 ** 9 + 7)
