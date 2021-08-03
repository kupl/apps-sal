import math


class Solution:
    def subarrayBitwiseORs(self, A: List[int]) -> int:
        ans = {A[0]}
        pre = {A[0]}
        for a in A[1:]:
            pre = {a | x for x in pre}
            pre.add(a)
            for i in pre:
                ans.add(i)
        return len(ans)
