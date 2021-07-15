class Solution:
    def subarrayBitwiseORs(self, A: List[int]) -> int:
        curr = {0}
        ans = set()
        for a in A:
            curr = {x|a for x in curr } | {a}
            ans |= curr
        return len(ans)
    

