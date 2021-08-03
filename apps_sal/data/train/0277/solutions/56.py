class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:
        n = len(light)
        states = [0] * n
        yellow_lights = set()
        all_blue_counter = 0

        for i in range(n):
            bulb = light[i] - 1

            if bulb == 0 or states[bulb - 1] == 2:
                states[bulb] = 2
            elif states[bulb - 1] != 2:
                states[bulb] = 1
                yellow_lights.add(bulb)

            if states[bulb] == 2:
                for j in range(bulb + 1, n):
                    if states[j] == 1:
                        yellow_lights.remove(j)
                        states[j] = 2
                    else:
                        break

            if len(yellow_lights) == 0:
                all_blue_counter += 1

        return all_blue_counter
