class Solution:

    def subarraysDivByK(self, A: List[int], K: int) -> int:
        P = [0]
        for x in A:
            P.append((P[-1] + x) % K)
        count = collections.Counter(P)
        ans = 0
        for v in list(count.values()):
            ans += int(v * (v - 1) * 0.5)
        return ans
