class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        seen = [0, 0, 0]
        for num in nums:
            for c in seen[:]:
                seen[(c + num) % 3] = max(seen[(c + num) % 3], c + num)
        return seen[0]
