class Solution:

    def subarrayBitwiseORs(self, A: List[int]) -> int:
        n = len(A)
        dp = set()
        ans = set()
        for j in range(n):
            dp_new = set()
            dp_new.add(A[j])
            for x in dp:
                dp_new.add(x | A[j])
            dp = dp_new
            ans.update(dp)
        return len(ans)
