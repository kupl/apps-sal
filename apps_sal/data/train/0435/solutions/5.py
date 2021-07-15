class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        n = len(A)
        pre = 0
        res = 0
        d = {0: 1}
        for a in A:
            pre = (pre + a) % K
            res += d.get(pre, 0)
            d[pre] = d.get(pre, 0) + 1
        return res
