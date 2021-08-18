

class Solution1:
    def maxSumDivThree(self, nums: List[int]) -> int:
        seen = [0, 0, 0]
        for a in nums:
            for i in seen[:]:
                seen[(i + a) % 3] = max(seen[(i + a) % 3], i + a)
        return seen[0]


class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        mod_1, mod_2, res, remove = [], [], 0, float('inf')
        for i in nums:
            if i % 3 == 0:
                res += i
            if i % 3 == 1:
                mod_1 += [i]
            if i % 3 == 2:
                mod_2 += [i]
        mod_1.sort(reverse=True)
        mod_2.sort(reverse=True)
        tmp = sum(mod_1) + sum(mod_2)
        if tmp % 3 == 0:
            return res + tmp
        elif tmp % 3 == 1:
            if len(mod_1):
                remove = min(remove, mod_1[-1])
            if len(mod_2) > 1:
                remove = min(mod_2[-1] + mod_2[-2], remove)
        elif tmp % 3 == 2:
            if len(mod_2):
                remove = min(remove, mod_2[-1])
            if len(mod_1) > 1:
                remove = min(mod_1[-1] + mod_1[-2], remove)
        return res + tmp - remove
