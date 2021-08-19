from math import floor, log


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ans = 0
        for x in nums:
            for i in bin(x)[2:]:
                if i != '0':
                    ans += 1
            # if floor(log(i, 2)) != log(i,2):
            #     # print(2**(floor(log(i, 2))), floor(log(i, 2)),i**(1/2), i)
            #     ans += i - (2**(floor(log(i, 2))))

        m = max(nums)
        ans += floor(log(m, 2))
        # print(floor(m**(1/2)))
        return ans
