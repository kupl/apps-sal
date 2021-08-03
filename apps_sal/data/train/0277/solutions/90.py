class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:
        max_ = 0
        output = 0
        for i in range(len(light)):
            max_ = max(max_, light[i])
            if max_ == i + 1:
                output += 1
        return output
