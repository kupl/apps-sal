class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:
        ans = 0
        m = 0
        for i, j in enumerate(light):
            m = max(m, j)
            if i + 1 == m:
                ans += 1
        return ans

