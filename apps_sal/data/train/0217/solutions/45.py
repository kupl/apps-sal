class Solution:
    def subarrayBitwiseORs(self, A: List[int]) -> int:
 
        cur = set()
        res = set()
        for i in A:
            temp = set([i])
            for j in cur:
                temp.add(i|j)
            cur = temp
            for j in cur:
                res.add(j)
        return len(res)
