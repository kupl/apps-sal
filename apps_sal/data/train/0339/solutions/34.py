from collections import Counter


class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        new1 = Counter(nums1)
        new2 = Counter(nums2)

        def helper(a, b):
            count = 0

            for key in a:
                target = key ** 2

                for kk in sorted(b.keys()):
                    c = target // kk

                    if c < kk:
                        break
                    elif c == kk:
                        count += b[kk] * (b[kk] - 1) * a[key] // 2
                    else:
                        if target % kk == 0 and c in b:
                            count += b[kk] * b[c] * a[key]

            return count

        return helper(new1, new2) + helper(new2, new1)
