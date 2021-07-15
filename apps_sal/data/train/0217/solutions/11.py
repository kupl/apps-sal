class Solution:
    def subarrayBitwiseORs(self, A: List[int]) -> int:
        cur, res = set(), set()
        for i in A:
            cur = {i | j for j in cur} | {i}
            res |= cur
        return len(res)
