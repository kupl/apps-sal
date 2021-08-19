class Solution:

    def numTimesAllBlue(self, light: List[int]) -> int:
        sum = total = count = 0
        for i in range(len(light)):
            sum += i + 1
            total += light[i]
            if sum == total:
                count += 1
        return count
