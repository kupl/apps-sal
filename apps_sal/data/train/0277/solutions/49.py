class Solution:

    def numTimesAllBlue(self, light: List[int]) -> int:
        min_off = 1
        max_on = float('-inf')
        count = 0
        blue = [0] * (len(light) + 1)
        for i in range(len(light)):
            blue[light[i]] = 1
            max_on = max(max_on, light[i])
            if light[i] == min_off:
                while min_off <= len(light) and blue[min_off] == 1:
                    min_off += 1
            if max_on < min_off:
                count += 1
        return count
