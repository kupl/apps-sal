class Solution:

    def minDays(self, n: int) -> int:
        queue = set([n])
        res = 0
        while queue:
            tmp = set()
            res += 1
            for a in queue:
                if a == 1:
                    return res
                if a % 2 == 0 and a // 2 not in queue:
                    tmp.add(a // 2)
                if a % 3 == 0 and a // 3 not in queue:
                    tmp.add(a // 3)
                tmp.add(a - 1)
            queue = tmp
        return res
