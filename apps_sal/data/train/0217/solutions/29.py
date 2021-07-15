class Solution:
    def subarrayBitwiseORs(self, A: List[int]) -> int:
        s = set()
        res = set()
        for x in A:
            new_s = {x}
            for xx in s:
                new_s.add(xx | x)
            s = new_s
            res |= s
        return len(res)
