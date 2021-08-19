class Solution:

    def subarrayBitwiseORs(self, A: List[int]) -> int:
        ans = set()
        cur = set()
        for x in A:
            cur = {y | x for y in cur} | set([x])
            ans |= cur
        return len(ans)
