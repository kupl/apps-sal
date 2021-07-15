class Solution:
    def subarrayBitwiseORs(self, A: List[int]) -> int:
        S, prev = set(), set()
        for a in A:
            temp = set()
            temp.add(a)
            S.add(a)
            for p in prev:
                temp.add(a|p)
                S.add(a|p)
            prev = temp
        return len(S)
