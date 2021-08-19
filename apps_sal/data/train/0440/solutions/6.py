class Solution:

    def mirrorReflection(self, p: int, q: int) -> int:
        targets = [(p, 0), (p, p), (0, p)]
        from fractions import Fraction
        x = y = 0
        (rx, ry) = (p, q)
        while (x, y) not in targets:
            t = float('inf')
            for v in [Fraction(-x, rx), Fraction(-y, ry), Fraction(p - x, rx), Fraction(p - y, ry)]:
                if v > 0:
                    t = min(t, v)
            (x, y) = (x + rx * t, y + ry * t)
            if x == p or x == 0:
                rx = -rx
            if y == p or y == 0:
                ry = -ry
        return targets.index((x, y))
