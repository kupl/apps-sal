class Solution:

    def subarrayBitwiseORs(self, A: List[int]) -> int:
        ans = set()
        previous = set()
        for v in A:
            current = set([i | v for i in previous])
            current.add(v)
            ans.update(current)
            previous = current
        return len(ans)
