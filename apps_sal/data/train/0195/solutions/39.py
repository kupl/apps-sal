from collections import Counter


class Solution:
    def countTriplets(self, A: List[int]) -> int:
        # https://leetcode.com/problems/triples-with-bitwise-and-equal-to-zero/discuss/227309/C%2B%2B-naive-O(n-*-n)
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
