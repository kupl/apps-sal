class Solution:

    def mirrorReflection(self, p: int, q: int) -> int:
        hm = {0: [p, 0], 1: [p, p], 2: [0, p]}
        slope = (q - p) / p
        if slope == 0:
            return 1
        start = [0, p]
        while start:
            x2 = start[0] - start[1] / slope
            if x2 <= p:
                start = [x2, p]
                for i in hm:
                    hm[i][1] = p - hm[i][1]
            else:
                y2 = start[1] + slope * (p - start[0])
                start = [0, y2]
                for i in hm:
                    hm[i][0] = p - hm[i][0]
            for k in hm:
                if hm[k] == [round(start[0], 5), round(start[1], 5)]:
                    return k
