class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        sumVal = sum(nums)
        if sumVal % 3 == 0:
            return sumVal
        categories = [[],[],[]]
        for num in nums:
            categories[num % 3].append(num)
        categories[1].sort()
        categories[2].sort()
        if sumVal % 3 == 1:
            if (len(categories[2]) < 2):
                return sumVal - categories[1][0]
            elif not categories[1]:
                return sumVal - categories[2][0] - categories[2][1]
            else:
                remainder = min(categories[1][0], categories[2][0] + categories[2][1])
                return sumVal - remainder
        else:
            if (len(categories[1]) < 2):
                return sumVal - categories[2][0]
            elif not categories[2]:
                return sumVal - categories[1][0] - categories[1][1]
            else:
                remainder = min(categories[2][0], categories[1][0] + categories[1][1])
                return sumVal - remainder

