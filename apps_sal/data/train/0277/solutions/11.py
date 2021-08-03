class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:
        left_most_off = 0
        right_most_on = -1
        state = [0] * len(light)
        res = 0
        for e in light:
            e -= 1
            state[e] = 1
            right_most_on = max(right_most_on, e)
            if e == left_most_off:
                while left_most_off < len(light) and state[left_most_off]:
                    left_most_off += 1
                if left_most_off == len(light) or left_most_off > right_most_on:
                    res += 1

        return res
