class Solution:
    def subarrayBitwiseORs(self, A: List[int]) -> int:

        res = set()
        tot = set()
        for a in A:
            res = {prev | a for prev in res} | {a}
            tot |= res
        return len(tot)
