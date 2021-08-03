class Solution:
    def subarrayBitwiseORs(self, A: List[int]) -> int:
        curr = set()
        ans = set()
        for x in A:
            curr = {x | y for y in curr} | {x}
            ans |= curr

        return len(ans)
