class Solution:
    def subarrayBitwiseORs(self, A: List[int]) -> int:
        ans = set()
        cur = set()
        for a in A:
            cur = {p | a for p in cur} | {a}
            ans |= cur
        return len(ans)
