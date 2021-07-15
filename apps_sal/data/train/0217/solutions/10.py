class Solution:
    def subarrayBitwiseORs(self, A: List[int]) -> int:
        ans = set()
        cur = {0}
        for i in A:
            cur = {i | y for y in cur} | {i}
            ans |= cur
        return len(ans)
