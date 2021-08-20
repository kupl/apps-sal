class Solution:

    def subarrayBitwiseORs(self, A: List[int]) -> int:
        st = set()
        cur = set()
        for a in A:
            cur = {b | a for b in cur} | {a}
            st |= cur
        return len(st)
