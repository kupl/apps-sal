class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:
        state = []  # on/off
        count = 0
        blue = 0
        last = 0

        for i in range(0, len(light)):
            state.append(False)

        for i, k in enumerate(light):
            state[k - 1] = True

            # count how many are blue
            for c in range(last, len(light)):
                if not state[c]:
                    last = c
                    break
                blue += 1

            if blue == i + 1:
                count += 1

        return count
