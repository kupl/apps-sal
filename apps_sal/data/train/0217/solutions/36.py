class Solution:

    def subarrayBitwiseORs(self, A: List[int]) -> int:
        (ans, dp) = (set(), set())
        for x in A:
            ndp = set()
            ndp.add(x)
            for y in dp:
                ndp.add(x | y)
                ans.add(y)
            dp = ndp
        for x in dp:
            ans.add(x)
        return len(ans)
