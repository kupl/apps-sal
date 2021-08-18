class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        res = 0
        sums = 0
        d = {0: 1}
        for num in A:
            sums = (sums + num) % K
            res += d.get(sums, 0)
            d[sums] = d.get(sums, 0) + 1
        return res
