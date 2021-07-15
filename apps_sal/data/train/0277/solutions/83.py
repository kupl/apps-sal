class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:
        res = right = 0
        for i, n in enumerate(light):
            # update right most bulb's number
            right = max(right, n)
            # right most bulb's number equals to number of processed bulbs
            # meaning all bulbs to the left are ON
            res += 1 if right == i + 1 else 0
        return res

