class Solution:

    def subarrayBitwiseORs(self, A: List[int]) -> int:
        ans = set()
        prev = set()
        for a in A:
            cur = set((a | b for b in prev))
            cur.add(a)
            prev = cur
            ans |= cur
        return len(ans)
