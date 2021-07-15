from collections import defaultdict

class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        if not A:
            return 0
        # Instead of actual prefix sums, store prefix sums mod K
        prefix_sums = defaultdict(list)
        prefix_sums[0].append(-1)
        cumsum = 0
        ans = 0
        for i, x in enumerate(A):
            cumsum += x
            cumsum_mod = cumsum % K
            ans += len(prefix_sums[cumsum_mod])
            prefix_sums[cumsum_mod].append(i)
        return ans
