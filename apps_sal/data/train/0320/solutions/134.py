class Solution:

    def minOperations(self, nums: List[int]) -> int:
        add = 0
        double = 0
        ans = 0
        for i in range(len(nums)):
            x = nums[i]
            if x == 0:
                continue
            add += 1
            curr = 0
            while x != 1:
                if x % 2 != 0:
                    x -= 1
                    add += 1
                while x % 2 != 1:
                    x /= 2
                    curr += 1
            double = max(double, curr)
        ans = double + add
        return ans
