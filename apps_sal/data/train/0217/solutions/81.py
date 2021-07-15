class Solution:
    def subarrayBitwiseORs(self, a: List[int]) -> int:
        res, prev = set(), set()
        res.add(a[0])
        prev.add(a[0])
        for i in range(1, len(a)):
            cur = set()
            cur.add(a[i])
            res.add(a[i])
            for j in prev:
                cur.add(j|a[i])
                res.add(j|a[i])
            prev = cur
        return len(res)
