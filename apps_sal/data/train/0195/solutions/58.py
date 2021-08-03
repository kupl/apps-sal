from collections import Counter


class Solution:
    def countTriplets(self, A: List[int]) -> int:
        c = Counter()

        for val in A:
            val = (~val) & 0xffff
            mask = val
            c[val] += 1

            while val > 0:
                val = (val - 1) & mask
                c[val] += 1

        ans = 0
        for v1 in A:
            for v2 in A:
                val = v1 & v2
                if val in c:
                    ans += c[val]
        return ans
