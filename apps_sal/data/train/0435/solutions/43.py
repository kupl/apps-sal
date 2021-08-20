class Solution:

    def subarraysDivByK(self, A: List[int], K: int) -> int:
        prefix = [0]
        for a in A:
            prefix += [(prefix[-1] + a) % K]
        cnt = collections.Counter(prefix)
        return int(sum((v * (v - 1) / 2 for v in list(cnt.values()))))
