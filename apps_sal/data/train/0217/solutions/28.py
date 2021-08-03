class Solution:
    def subarrayBitwiseORs(self, A: List[int]) -> int:

        result = set()
        cur = {0}

        for x in A:
            cur = {x | y for y in cur} | {x}
            result |= cur

        return len(result)
