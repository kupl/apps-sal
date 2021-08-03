from collections import Counter


class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        presum = [0]
        for num in A:
            presum.append((presum[-1] + num) % K)

        count = Counter(presum)
        return sum(c * (c - 1) // 2 for c in list(count.values()))
