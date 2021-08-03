import math


class Solution:
    def subarrayBitwiseORs(self, A: List[int]) -> int:
        ans = {A[0]}
        pre = {A[0]}
        for a in A[1:]:
            pre = {a | x for x in pre}
            pre.add(a)
            ans.update(pre)
        return len(ans)
