class Solution:
    def subarrayBitwiseORs(self, A: List[int]) -> int:
        s = set()
        c = set()
        for x in A:
            c = {x | y for y in c}
            c.add(x)
            s |= c
        return len(s)
