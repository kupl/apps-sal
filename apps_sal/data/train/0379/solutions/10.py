class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        dp1, dp2 = collections.defaultdict(lambda: 0), collections.defaultdict(lambda: 0)
        i = j = 0

        while i < len(nums1) and j < len(nums2):
            x, y = nums1[i], nums2[j]
            if x < y:
                if i == 0:
                    dp1[x] = dp2[y] + x
                else:
                    dp1[x] = max(dp1[nums1[i - 1]], dp2[y]) + x
                i += 1
            elif x > y:
                if j == 0:
                    dp2[y] = dp1[x] + y
                else:
                    dp2[y] = max(dp2[nums2[j - 1]], dp1[x]) + y
                j += 1
            else:
                dp1[x] = max((dp2[nums2[j - 1]] if j != 0 else 0) + x, (dp1[nums1[i - 1]] if i != 0 else 0) + x)
                dp2[y] = max((dp1[nums1[i - 1]] if i != 0 else 0) + y, (dp2[nums2[j - 1]] if j != 0 else 0) + y)
                i += 1
                j += 1

        x, y = max(dp1.values()), max(dp2.values())

        while i < len(nums1):
            x += nums1[i]
            i += 1

        while j < len(nums2):
            y += nums2[j]
            j += 1

        return max(x, y) % (10 ** 9 + 7)
