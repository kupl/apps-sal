class Solution:

    def subarrayBitwiseORs(self, A: List[int]) -> int:
        res = set([])
        tmp = set([])
        for i in A:
            newtmp = set([])
            for j in tmp:
                newtmp.add(i | j)
                res.add(i | j)
            newtmp.add(i)
            res.add(i)
            tmp = newtmp
        return len(res)
