class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        states = [0, float('-inf'), float('-inf')]

        for n in nums:
            old = states[:]
            for i in range(3):
                states[(i + n) % 3] = max(old[(i + n) % 3], old[i] + n)

        return states[0]
