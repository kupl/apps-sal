class Solution:
    def minOperations(self, nums: List[int]) -> int:
        adds = []
        muls = []

        for idx, num in enumerate(nums):
            adds.append(0)
            muls.append(0)
            while num > 0:
                if num % 2 == 1:
                    adds[idx] += 1
                    num -= 1
                else:
                    muls[idx] += 1
                    num /= 2

        return sum(adds) + max(muls)
