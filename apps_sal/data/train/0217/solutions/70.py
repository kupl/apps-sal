class Solution:
    def subarrayBitwiseORs(self, A: List[int]) -> int:
        res = set()
        cur = set()
        for a in A:
            cur = {n | a for n in cur} | {a}
            res |= cur
        return len(res)
