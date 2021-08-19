from collections import defaultdict


class Solution:

    def subarraysDivByK(self, A: List[int], K: int) -> int:
        if not A:
            return 0
        prefix_sums = defaultdict(int)
        prefix_sums[0] = 1
        cumsum = 0
        ans = 0
        for (i, x) in enumerate(A):
            cumsum = (cumsum + x) % K
            ans += prefix_sums[cumsum]
            prefix_sums[cumsum] += 1
        return ans
