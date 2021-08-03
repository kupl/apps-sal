class Solution:
    def minDays(self, n: int) -> int:
        step = 0
        cur = {n}
        while 0 not in cur:
            new_cur = set()
            for i in cur:
                new_cur.add(i - 1)
                if not i % 2:
                    new_cur.add(i // 2)
                if not i % 3:
                    new_cur.add(i // 3)
            cur = new_cur
            step += 1
        return step
