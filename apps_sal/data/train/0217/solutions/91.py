class Solution:
    def subarrayBitwiseORs(self, A: List[int]) -> int:
        res = set()

        cur = set()

        for x in A:
            cur = {x} | {x | y for y in cur}
            res |= cur

        return len(res)
