class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:
        return sum(i == m for i, m in enumerate(itertools.accumulate(light, max), 1))
