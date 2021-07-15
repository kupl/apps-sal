class Solution:
    def minDays(self, n: int) -> int:
        buf = {n}
        for i in range(1, n + 1):
            if 1 in buf: return i
            old, buf = buf, set()
            for x in old:
                buf.add(x - 1)
                if x % 2 == 0: buf.add(x // 2)
                if x % 3 == 0: buf.add(x // 3)

