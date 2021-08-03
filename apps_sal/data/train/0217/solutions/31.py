class Solution:
    def subarrayBitwiseORs(self, A: List[int]) -> int:
        cur, res = set(), set()
        for a in A:
            cur = {a | b for b in cur} | {a}
            res |= cur
        return len(res)
