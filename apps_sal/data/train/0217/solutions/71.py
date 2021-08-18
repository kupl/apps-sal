class Solution:
    def subarrayBitwiseORs(self, A: List[int]) -> int:
        s = set()
        s1 = set()
        for n in A:
            s2 = set()
            for e in s1:
                s2.add(e | n)
            s1 = s2
            s1.add(n)
            s |= s1
        return len(s)
