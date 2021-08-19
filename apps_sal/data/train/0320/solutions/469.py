from typing import List


class Counter:

    def __init__(self):
        self.c = 0


class Solution:

    def minOperations(self, nums: List[int]) -> int:

        def makeAllEven(nums, counter):

            def decrease(num, counter):
                if num % 2 != 0:
                    num -= 1
                    counter.c += 1
                return num
            ret = list(map(lambda n: decrease(n, counter), nums))
            return ret

        def allZero(nums):
            return sum(nums) == 0

        def makeAllHalf(nums, counter):
            ret = list(map(lambda x: x // 2, nums))
            counter.c += 1
            return ret
        counter = Counter()
        while not allZero(nums):
            nums = makeAllEven(nums, counter)
            if not allZero(nums):
                nums = makeAllHalf(nums, counter)
        return counter.c
