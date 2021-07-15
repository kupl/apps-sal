class Solution:
    def subarrayBitwiseORs(self, A: List[int]) -> int:
        result, curr = set(), set()
        for a in A:
            curr = {a | j for j in curr} | {a}
            result |= curr
        return len(result)
