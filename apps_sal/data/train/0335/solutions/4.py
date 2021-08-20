class Solution:

    def exclu(self, nums):
        n = len(nums)
        if n <= 1:
            return False
        if n <= 4:
            for x in nums:
                for y in nums:
                    if x & y == 0:
                        return True
            return False
        (set0, set1) = (set(), set())
        for x in nums:
            if x & 1:
                set1.add(x >> 1)
            else:
                set0.add(x >> 1)
        if set0:
            if self.exclu(set0):
                return True
            if set1:
                return self.exclu2(set0, set1)
        return False

    def exclu2(self, set0, set1):
        if len(set0) == 0 or len(set1) == 0:
            return False
        if len(set1) == 1:
            x = next(iter(set1))
            for y in set0:
                if x & y == 0:
                    return True
            return False
        if len(set0) == 1:
            x = next(iter(set0))
            for y in set1:
                if x & y == 0:
                    return True
            return False
        if len(set0) <= 8 and len(set1) <= 8:
            for x in set0:
                for y in set1:
                    if x & y == 0:
                        return True
            return False
        (set00, setx0, set01, set11) = (set(), set(), set(), set())
        for x in set0:
            setx0.add(x >> 1)
            if x & 1 == 0:
                set00.add(x >> 1)
        for x in set1:
            if x & 1:
                set11.add(x >> 1)
            else:
                set01.add(x >> 1)
        if set00 and set11 and self.exclu2(set00, set11):
            return True
        if set01 and setx0 and self.exclu2(set01, setx0):
            return True
        return False

    def tallestBillboard(self, rods: List[int]) -> int:
        n = len(rods)
        if n <= 1:
            return 0
        t = sum(rods)
        m = t // 2
        infos = [[] for _ in range(m + 1)]
        infos[0] = [0]
        b = 1
        for x in rods:
            for y in range(m - x, -1, -1):
                comb = infos[y]
                if comb:
                    infos[x + y] += [z + b for z in comb]
            b *= 2
        for y in range(m, 0, -1):
            (comb, n) = (infos[y], len(infos[y]))
            if n >= 2:
                if self.exclu(comb):
                    return y
        return 0
