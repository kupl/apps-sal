class Solution:

    def numTimesAllBlue(self, light: List[int]) -> int:
        n = max(light)
        bulb_status = ['off'] * (n + 1)
        count = 0
        num_on = 0
        num_blue = 0
        for i in light:
            bulb_status[i] = 'on'
            num_on += 1
            while i <= n and (i == 1 or bulb_status[i - 1] == 'blue'):
                if bulb_status[i] == 'off':
                    break
                bulb_status[i] = 'blue'
                num_blue += 1
                num_on -= 1
                i += 1
            if num_on == 0 and num_blue > 0:
                count += 1
        return count
