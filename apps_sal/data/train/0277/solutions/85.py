class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:
        bulb_ranges = {}
        lights_on = 0
        result = 0
        for l in light:
            lights_on += 1
            left = right = None
            if l - 1 not in bulb_ranges and l + 1 not in bulb_ranges:
                left = l
                right = l
            else:
                if l - 1 in bulb_ranges:
                    cur_left, cur_right = bulb_ranges[l - 1]
                    left = cur_left
                    right = l
                    del bulb_ranges[l - 1]
                if l + 1 in bulb_ranges:
                    cur_left, cur_right = bulb_ranges[l + 1]
                    if left is None:
                        left = l
                    right = cur_right
                    del bulb_ranges[l + 1]

            bulb_ranges[left] = (left, right)
            bulb_ranges[right] = (left, right)
            if left == 1 and right - left + 1 == lights_on:
                result += 1

        return result
