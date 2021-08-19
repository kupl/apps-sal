class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:

        @lru_cache(None)
        def recurse(i, pos):
            if pos < 0:
                if i == 0:
                    return 0
                return -10000000

            temp = max(nums[pos] + recurse((i + nums[pos]) % 3, pos - 1), recurse((i) % 3, pos - 1))

            # print(i,pos,temp)
            return temp

        return recurse(0, len(nums) - 1)
