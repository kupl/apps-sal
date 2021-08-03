class Solution:
    def minDays(self, n: int) -> int:
        s = {n}
        for i in itertools.count(1):
            if 1 in s:
                return i
            nxt = set()
            for x in s:
                nxt.add(x - 1)
                if x % 2 == 0:
                    nxt.add(x >> 1)
                if x % 3 == 0:
                    nxt.add(x // 3)
            s = nxt
