class Solution:
    def minDays(self, n: int) -> int:
        q = [n]
        res = 0
        while q:
            tmp = set()
            for curr in q:
                if curr == 0:
                    return res
                tmp.add(curr-1)
                if curr % 3 == 0:
                    tmp.add(curr//3)
                if curr % 2 == 0:
                    tmp.add(curr//2)
            q = tmp
            res += 1
        return res
