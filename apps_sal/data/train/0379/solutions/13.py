class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        m = len(nums1)
        n = len(nums2)
        i = m - 1
        j = n - 1
        s1 = 0
        s2 = 0
        while(i >= 0 and j >= 0):
            if(nums1[i] > nums2[j]):
                s1 += nums1[i]
                i -= 1
            elif(nums2[j] > nums1[i]):
                s2 += nums2[j]
                j -= 1
            else:
                s1 = max(s1, s2) + nums1[i]
                s2 = s1
                i -= 1
                j -= 1
        if(i != -1):
            s1 += sum(nums1[:i + 1])
        if(j != -1):
            s2 += sum(nums2[:j + 1])
        return max(s1, s2) % (10**9 + 7)
