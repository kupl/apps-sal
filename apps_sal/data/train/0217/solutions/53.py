class Solution:
    def subarrayBitwiseORs(self, A: List[int]) -> int:

        curr = set()
        ans = set()
        for a in A:
            s = set()
            s.add(a)
            for i in curr:
                s.add(a | i)
            curr = s
            for t in curr:
                ans.add(t | a)
        return len(ans)
