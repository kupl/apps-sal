class Solution:
    def subarrayBitwiseORs(self, A: List[int]) -> int:
        # Frontier Set
        # Time  complexity: O(NlogW), where N is the length of A, and W is the maximum size of elements in A.
        # Space complexity: O(NlogW)
        ans = set()
        cur = {0}
        for x in A:
            cur = {x | y for y in cur} | {x}
            ans |= cur
        return len(ans)
