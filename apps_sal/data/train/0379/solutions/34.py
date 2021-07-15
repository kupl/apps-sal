class Solution:
    def maxSum(self, nums1, nums2):
        M, N = len(nums1), len(nums2)
        sum1, sum2 = 0, 0
        i, j = 0, 0
        res = 0
        
        while i < M and j < N:
            if nums1[i] < nums2[j]:
                sum1 += nums1[i]
                i += 1
            elif nums1[i] > nums2[j]:
                sum2 += nums2[j]
                j += 1
            else:
                res += max(sum1, sum2) + nums1[i]
                i += 1
                j += 1
                sum1 = 0
                sum2 = 0
                
        while i < M:
            sum1 += nums1[i]
            i += 1
        while j < N:
            sum2 += nums2[j]
            j += 1
        return (res + max(sum1, sum2)) % 1000000007

