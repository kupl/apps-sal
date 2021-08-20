class Solution:

    def minDays(self, n: int) -> int:
        i = 1
        c_set = {n}
        while 1 not in c_set:
            new_set = set()
            for a in c_set:
                new_set.add(a - 1)
                if a % 2 == 0:
                    new_set.add(a // 2)
                if a % 3 == 0:
                    new_set.add(a // 3)
            c_set = new_set
            i += 1
        return i
