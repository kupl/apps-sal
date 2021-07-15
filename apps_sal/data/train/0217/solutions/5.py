class Solution:
    def subarrayBitwiseORs(self, A: List[int]) -> int:
        results = set()
        curr = {0}
        for a in A:
            curr = {a | b for b in curr} | {a}
            results |= curr
        return len(results)

