class Solution:

    def subarrayBitwiseORs(self, A: List[int]) -> int:
        (s, ans) = (set(), set())
        for a in A:
            s = {a} | {a | b for b in s}
            ans |= s
        return len(ans)
