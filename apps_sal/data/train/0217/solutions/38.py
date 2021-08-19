class Solution:

    def subarrayBitwiseORs(self, A: List[int]) -> int:
        ans = set()
        tp = set()
        tp.add(0)
        for i in A:
            tpp = set()
            tpp.add(i)
            for ii in tp:
                tpp.add(ii | i)
            tp = tpp
            for ii in tp:
                ans.add(ii)
        return len(ans)
