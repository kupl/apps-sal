class Solution:

    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        (cnt1, cnt2) = (collections.Counter(nums1), collections.Counter(nums2))
        ans = 0
        for (v1, l1) in list(cnt1.items()):
            for (v2, l2) in list(cnt2.items()):
                if v2 != v1 and v1 ** 2 / v2 in cnt2:
                    ans += l1 * l2 * cnt2[v1 ** 2 / v2]
                elif v2 == v1:
                    ans += l1 * l2 * (l2 - 1)
        for (v1, l1) in list(cnt2.items()):
            for (v2, l2) in list(cnt1.items()):
                if v2 != v1 and v1 ** 2 / v2 in cnt1:
                    ans += l1 * l2 * cnt1[v1 ** 2 / v2]
                elif v2 == v1:
                    ans += l1 * l2 * (l2 - 1)
        return int(ans / 2)
