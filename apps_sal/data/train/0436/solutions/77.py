class Solution:
    def minDays(self, n: int) -> int:
        q, res, seen = [n], 0, set()
        while q:
            tmp = set()
            if 0 in q:
                return res
            for p in q:
                if p - 1 not in seen:
                    tmp.add(p - 1)
                    seen.add(p - 1)
                if p % 3 == 0 and p // 3 not in seen:
                    tmp.add(p // 3)
                    seen.add(p // 3)
                if p % 2 == 0 and p // 2 not in seen:
                    tmp.add(p // 2)
                    seen.add(p // 2)
            q = tmp
            res += 1
        return res
