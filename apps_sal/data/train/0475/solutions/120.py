class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        combinations = []

        for i in range(n):
            combinations.append(nums[i])
            for j in range(i + 1, n):
                combinations.append(combinations[-1] + nums[j])

        combinations.sort()

        sum_nos = 0
        for index in range(left - 1, right):
            sum_nos += combinations[index]

        return sum_nos % (10 ** 9 + 7)
