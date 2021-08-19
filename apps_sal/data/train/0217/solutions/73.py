class Solution:
    def subarrayBitwiseORs(self, A: List[int]) -> int:
        # 12:57 8/24/20

        res, cur = set(), set()
        for i in A:
            cur = {i | j for j in cur} | {i}
            res |= cur
        return len(res)
