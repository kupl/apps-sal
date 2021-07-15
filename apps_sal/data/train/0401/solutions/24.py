class Solution:
    def maxSumDivThree(self, nums):

        total =     sum(nums)
        mod_total = total % 3 

        if mod_total == 0:
            return total

        else:

            def min_n(nums, n):
                if len(nums) < n: return 10**6
                sum_n = 0
                for i in range(n):
                    min_current = min(nums)
                    min_current_ind = nums.index(min_current)
                    sum_n += nums.pop(min_current_ind)
                return sum_n

            mod_1 = [e for e in nums if e % 3 == 1]
            mod_2 = [e for e in nums if e % 3 == 2]

            if mod_total == 1:

                one_mod_1 =   min_n(mod_1, 1)
                two_mod_2 =   min_n(mod_2, 2)

                return total - min(one_mod_1, two_mod_2)

            elif mod_total == 2:

                two_mod_1 =   min_n(mod_1, 2)
                one_mod_2 =   min_n(mod_2, 1)

                return total - min(two_mod_1, one_mod_2)

