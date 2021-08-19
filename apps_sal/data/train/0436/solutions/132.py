class Solution:

    def minDays(self, n: int) -> int:
        d = 1
        poss = set([n])
        while 1 not in poss:
            d += 1
            new_poss = set()
            for i in poss:
                new_poss.add(i - 1)
                if i % 2 == 0:
                    new_poss.add(i // 2)
                if i % 3 == 0:
                    new_poss.add(i // 3)
            poss = new_poss
        return d
