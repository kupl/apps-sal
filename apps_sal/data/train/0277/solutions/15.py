class Solution:

    def numTimesAllBlue(self, light: List[int]) -> int:
        on = [False] * len(light)
        n = len(light)
        (blue, ans) = (0, 0)
        for i in range(0, n):
            on[light[i] - 1] = True
            while blue < n and on[blue] == True:
                blue += 1
            if blue == i + 1:
                ans += 1
        return ans
