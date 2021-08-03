class Solution:
    def smallestRepunitDivByK(self, K: int) -> int:
        remainders = set([0])
        ans = repunit = 1
        while repunit % K not in remainders:
            repunit %= K
            remainders.add(repunit)
            repunit = repunit * 10 + 1
            ans += 1
        return ans if repunit % K == 0 else -1
