class Solution:
    def minDays(self, n: int) -> int:
        days = 0
        s0 = set()
        s1 = set()
        s1.add(n)
        while True:
            days += 1
            for si in s1:
                if si == 1:
                    return days
                if si % 2 == 0:
                    s0.add(si // 2)
                if si % 3 == 0:
                    s0.add(si - 2 * (si / 3))
                s0.add(si - 1)
            s1 = s0
            s0 = set()
