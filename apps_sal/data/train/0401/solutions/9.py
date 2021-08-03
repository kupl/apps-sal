class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        seen = [0, 0, 0]
        for n in nums:
            for i in seen[:]:
                seen[(n + i) % 3] = max(seen[(n + i) % 3], i + n)

        return seen[0]
