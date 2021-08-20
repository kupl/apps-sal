class Solution:

    def subarrayBitwiseORs(self, A: List[int]) -> int:
        res = set()
        cur = set()
        for a in A:
            cur = {a | i for i in cur}
            cur |= {a}
            res |= cur
        return len(res)
