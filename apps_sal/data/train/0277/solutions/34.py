class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:
        n = len(light)
        ans = 0
        bulbs = [0 for _ in range(n)]
        zero_i, one_i = 0, 0
        for i in light:
            bulbs[i - 1] = 1
            if zero_i == i - 1:
                j = i - 1
                while j < n and bulbs[j] == 1:
                    j += 1
                zero_i = j
            one_i = max(one_i, i - 1)
            if one_i < zero_i:
                ans += 1

        return ans
