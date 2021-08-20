class Solution:

    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        arr = [[-math.inf for i in range(len(nums1) + 1)] for j in range(len(nums2) + 1)]
        for i in range(len(nums2) + 1):
            arr[i][0] = -math.inf
        for i in range(len(nums1) + 1):
            arr[0][i] = -math.inf
        maxc = nums2[0] * nums1[0]
        for i in range(len(nums2) + 1)[1:]:
            for j in range(len(nums1) + 1)[1:]:
                arr[i][j] = max(arr[i][j], arr[i][j - 1])
                arr[i][j] = max(arr[i][j], arr[i - 1][j])
                arr[i][j] = max(arr[i][j], max(arr[i - 1][j - 1], 0) + nums2[i - 1] * nums1[j - 1])
                if arr[i][j] > maxc:
                    maxc = arr[i][j]
        return maxc
