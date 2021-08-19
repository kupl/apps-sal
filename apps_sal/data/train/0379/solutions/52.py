class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        # Represents the max value (looking ahead) from this node
        dp1 = [0 for _ in range(len(nums1))] + [0]
        dp2 = [0 for _ in range(len(nums2))] + [0]

        nums1.append(0)
        nums2.append(0)

        for i in range(len(nums1) - 2, -1, -1):
            dp1[i] = (dp1[i + 1] + nums1[i + 1])

        for i in range(len(nums2) - 2, -1, -1):
            dp2[i] = (dp2[i + 1] + nums2[i + 1])

        i, j = len(nums1) - 2, len(nums2) - 2

        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                dp1[i] = (nums1[i + 1] + dp1[i + 1])
                i -= 1
            elif nums1[i] < nums2[j]:
                dp2[j] = (nums2[j + 1] + dp2[j + 1])
                j -= 1
            else:
                # Find which one has the greater parent
                max_value = max(dp1[i + 1] + nums1[i + 1], dp2[j + 1] + nums2[j + 1])
                dp1[i] = max_value
                dp2[j] = max_value

                j -= 1
                i -= 1

        while i >= 0:
            dp1[i] = (nums1[i + 1] + dp1[i + 1])
            i -= 1

        while j >= 0:
            dp2[j] = (nums2[j + 1] + dp2[j + 1])
            j -= 1

        return max((dp1[0] + nums1[0]) % (10**9 + 7), (dp2[0] + nums2[0]) % (10**9 + 7))
