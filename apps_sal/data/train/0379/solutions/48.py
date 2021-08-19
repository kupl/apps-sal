class Solution:

    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        intersecting_index = []
        l = 0
        m = 0
        while l < len(nums1) and m < len(nums2):
            if nums1[l] == nums2[m]:
                intersecting_index.append([l, m])
                l += 1
                m += 1
            elif nums1[l] > nums2[m]:
                m += 1
            else:
                l += 1
        prefix_1 = [0 for i in range(len(nums1) + 1)]
        prefix_2 = [0 for i in range(len(nums2) + 1)]
        for i in range(1, len(nums1) + 1):
            prefix_1[i] = prefix_1[i - 1] + nums1[i - 1]
        for i in range(1, len(nums2) + 1):
            prefix_2[i] = prefix_2[i - 1] + nums2[i - 1]
        ans = []
        prev_1 = 0
        prev_2 = 0
        for i in intersecting_index:
            ans.append([prefix_1[i[0] + 1] - prefix_1[prev_1], prefix_2[i[1] + 1] - prefix_2[prev_2]])
            prev_1 = i[0] + 1
            prev_2 = i[1] + 1
        ans.append([prefix_1[-1] - prefix_1[prev_1], prefix_2[-1] - prefix_2[prev_2]])
        s = 0
        for i in ans:
            s = (max(i[0], i[1]) + s) % (pow(10, 9) + 7)
        return s
