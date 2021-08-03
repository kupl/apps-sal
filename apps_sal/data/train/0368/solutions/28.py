class Solution:
    def maxSatisfaction(self, sat: List[int]) -> int:
        sat = sorted(sat)
        out = [0]
        while len(sat) > 0:
            value = 0
            for i, v in enumerate(sat):
                value += v * (i + 1)
            out.append(value)
            print(sat)
            if sat[0] > 0:
                break
            sat = sat[1:]
        return max(out)
