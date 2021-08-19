class Solution:

    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        sum_set = set()
        sum_set.add(0)
        temp = 0
        count = 0
        for num in nums:
            temp += num
            if temp - target in sum_set:
                count += 1
                sum_set.clear()
                sum_set.add(0)
                temp = 0
                continue
            sum_set.add(temp)
        return count
