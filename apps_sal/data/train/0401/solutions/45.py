class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        total = sum(nums)
        mod = total % 3
        if mod == 0:
            return total
        min_2 = defaultdict(list)
        for num in nums:
            if num % 3 == 1:
                min_2[1].append(num)
                min_2[1].sort()
                if len(min_2[1]) > 2:
                    min_2[1].pop()
            elif num % 3 == 2:
                min_2[2].append(num)
                min_2[2].sort()
                if len(min_2[2]) > 2:
                    min_2[2].pop()
        res = 0
        if mod == 1:
            if len(min_2[1]) >= 1:
                res = total - min_2[1][0]
            if len(min_2[2]) >= 2:
                res = max(res, total - min_2[2][0] - min_2[2][1])
            return res
        if len(min_2[2]) >= 1:
            res = total - min_2[2][0]
        if len(min_2[1]) >= 2:
            res = max(res, total - min_2[1][0] - min_2[1][1])
        return res
