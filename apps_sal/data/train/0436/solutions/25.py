class Solution:

    def minDays(self, n: int) -> int:
        l = {n}
        count = 0
        while not l.__contains__(0):
            count += 1
            t = set()
            for i in l:
                t.add(i - 1)
                if i % 2 == 0:
                    t.add(i / 2)
                if i % 3 == 0:
                    t.add(i / 3)
            l = t
        return count
