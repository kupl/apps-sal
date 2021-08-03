class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        mod_one = [-1, -1]
        mod_two = [-1, -1]
        total_sum = 0
        for x in nums:
            total_sum += x
            if x % 3 == 1:
                if mod_one[0] == -1 or x < mod_one[0]:
                    mod_one[1] = mod_one[0]
                    mod_one[0] = x
                elif mod_one[1] == -1 or x < mod_one[1]:
                    mod_one[1] = x
            elif x % 3 == 2:
                if mod_two[0] == -1 or x < mod_two[0]:
                    mod_two[1] = mod_two[0]
                    mod_two[0] = x
                elif mod_two[1] == -1 or x < mod_two[1]:
                    mod_two[1] = x

        if total_sum % 3 == 0:
            return total_sum
        elif total_sum % 3 == 1:
            if mod_one[0] != -1 and (mod_two[0] == -1 or mod_two[1] == -1 or mod_one[0] < sum(mod_two)):
                return total_sum - mod_one[0]
            elif mod_two[0] != -1 and mod_two[1] != -1:
                return total_sum - sum(mod_two)
            else:
                return 0
        else:
            if mod_two[0] != -1 and (mod_one[0] == -1 or mod_one[1] == -1 or mod_two[0] < sum(mod_one)):
                return total_sum - mod_two[0]
            elif mod_one[0] != -1 and mod_one[1] != -1:
                return total_sum - sum(mod_one)
            else:
                return 0
