class Solution:
    def subarrayBitwiseORs(self, A: List[int]) -> int:
        s = set()
        res = set()
        for n in A:
            s = {n} | {n | el for el in s}
            res |= s

        return len(res)
