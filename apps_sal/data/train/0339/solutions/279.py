class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        count1 = collections.Counter(nums1)
        count2 = collections.Counter(nums2)

        def cal(nums1, count2):
            ans = 0
            for n1 in nums1:
                sq = n1**2
                for n2 in sorted(count2):
                    if sq % n2 != 0 or sq // n2 not in count2:
                        continue
                    c2 = sq // n2
                    if c2 < n2:
                        break
                    elif c2 == n2 and count2[n2] > 1:
                        ans += math.comb(count2[n2], 2)
                    elif c2 > n2:
                        ans += count2[n2] * count2[c2]

            return ans

        return cal(nums1, count2) + cal(nums2, count1)
