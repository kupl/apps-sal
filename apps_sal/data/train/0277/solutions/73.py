class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:
        total = 0
        count = 0
        for k in range(len(light)):
            total += light[k]
            if total == ((k + 1) * (k + 2)) // 2:
                count += 1
        return count
