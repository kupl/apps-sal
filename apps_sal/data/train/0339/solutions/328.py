from collections import defaultdict
from typing import List


class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        # ハッシュ化
        h1 = {}
        h2 = {}

        for n in nums1:
            if n in h1:
                h1[n] += 1
            else:
                h1[n] = 1
        for n in nums2:
            if n in h2:
                h2[n] += 1
            else:
                h2[n] = 1

        count = 0

        # Type1
        for n in nums1:
            n2 = n * n
            for v in list(h2.keys()):
                q, m = divmod(n2, v)
                if m != 0 or q not in h2:
                    continue

                l1 = h2[v]
                if v == q:
                    if l1 > 1:
                        # l1個の中から2個選ぶ組み合わせの数
                        count += (l1 * (l1 - 1))
                else:
                    l2 = h2[q]
                    count += l1 * l2

        # Type2
        for n in nums2:
            n2 = n * n
            for v in list(h1.keys()):
                q, m = divmod(n2, v)
                if m != 0 or q not in h1:
                    continue

                l1 = h1[v]
                if v == q:
                    if l1 > 1:
                        # l1個の中から2個選ぶ組み合わせの数
                        count += (l1 * (l1 - 1))
                else:
                    l2 = h1[q]
                    count += l1 * l2

        return int(count / 2)
