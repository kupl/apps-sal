class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:

        min_counter = -1
        max_counter = -1

        turned_on = [0] * len(light)

        moments = 0
        for bulb in light:
            bulb = bulb - 1
            max_counter = max(max_counter, bulb)
            turned_on[bulb] = 1

            while min_counter + 1 < len(turned_on) and turned_on[min_counter + 1] == 1:
                min_counter += 1

            if max_counter == min_counter:
                moments += 1

        return moments
