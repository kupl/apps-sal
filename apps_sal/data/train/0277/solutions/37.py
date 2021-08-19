class Solution:

    def numTimesAllBlue(self, light: List[int]) -> int:
        n = len(light)
        rMin = [light[-1]] * n
        for i in range(n - 2, -1, -1):
            rMin[i] = min(rMin[i + 1], light[i])
        out = 1
        lmax = 0
        for i in range(n - 1):
            lmax = max(lmax, light[i])
            if lmax <= rMin[i + 1]:
                out += 1
        return out
