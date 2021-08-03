class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        res = 0
        ls = len(nums)
        for i in range(ls):
            divs = set()
            for j in range(1, floor(sqrt(nums[i])) + 1):
                if nums[i] % j == 0:
                    divs.add(nums[i] // j)
                    divs.add(j)

            if len(divs) == 4:
                res = res + sum(divs)
        return res
