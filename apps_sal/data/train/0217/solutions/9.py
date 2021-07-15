class Solution:
    def subarrayBitwiseORs(self, A: List[int]) -> int:
        cur = set()
        all = set()
        for v in A:
            cur = set(e | v for e in cur)
            cur.add(v)
            all |= cur
        return len(all)
