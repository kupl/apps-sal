class Solution:

    def mirrorReflection(self, p: int, q: int) -> int:

        def determine_reflect_point(x1, y1, x2, y2):
            slope = (y2 - y1) / (x2 - x1)
            ref_slope = -slope
            if abs(x2 - p) < 10 ** (-2):
                val1 = [0, y2 + ref_slope * -p]
                val2 = [(0 - y2) / ref_slope + p, 0]
                val3 = [(p - y2) / ref_slope + p, p]
            if abs(x2) < 10 ** (-2):
                val1 = [p, y2 + ref_slope * p]
                val2 = [(0 - y2) / ref_slope + 0, 0]
                val3 = [(p - y2) / ref_slope + 0, p]
            if abs(y2) < 10 ** (-2):
                val1 = [p, ref_slope * (p - x2)]
                val2 = [0, ref_slope * (0 - x2)]
                val3 = [(p - 0) / ref_slope + x2, p]
            if abs(y2 - p) < 10 ** (-2):
                val1 = [p, p + ref_slope * (p - x2)]
                val2 = [0, p + ref_slope * (0 - x2)]
                val3 = [x2, p]
            if 0 <= val1[0] <= p and 0 <= val1[1] <= p:
                return (x2, y2, val1[0], val1[1])
            if 0 <= val2[0] <= p and 0 <= val2[1] <= p:
                return (x2, y2, val2[0], val2[1])
            if 0 <= val3[0] <= p and 0 <= val3[1] <= p:
                return (x2, y2, val3[0], val3[1])
        p1 = [0, 0]
        p2 = [p, q]
        while True:
            if abs(p2[0] - 0) < 10 ** (-2) and abs(p2[1] - p) < 10 ** (-2):
                return 2
            if abs(p2[0] - p) < 10 ** (-2) and p2[1] - 0 < 10 ** (-2):
                return 0
            if abs(p2[0] - p) < 10 ** (-2) and abs(p2[1] - p) < 10 ** (-2):
                return 1
            (p1[0], p1[1], p2[0], p2[1]) = determine_reflect_point(p1[0], p1[1], p2[0], p2[1])
