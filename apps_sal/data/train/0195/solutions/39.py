from collections import Counter


class Solution:
    def countTriplets(self, A: List[int]) -> int:
        cnt = Counter()
        for a in A:
            for b in A:
                cnt[a & b] += 1

        res = 0
        for a in A:
            for k, v in cnt.items():
                if a & k == 0:
                    res += v

        return res
