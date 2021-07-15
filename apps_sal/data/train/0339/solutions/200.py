class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        import collections
        h1 = {}
        s1 = collections.Counter()
        h2 = {}
        s2 = collections.Counter()
        for i in range(len(nums1)):
            for j in range(i + 1, len(nums1)):
                s1[nums1[i]*nums1[j]] += 1
                h1[(i, j)] = nums1[i]*nums1[j]
                
        for i in range(len(nums2)):
            for j in range(i + 1, len(nums2)):
                s2[nums2[i]*nums2[j]] += 1
                h2[(i, j)] = nums2[i]*nums2[j]
        ans = 0
        for i in range(len(nums1)):
            if nums1[i]*nums1[i] in s2:
                ans += s2[nums1[i]*nums1[i]]
                
        for i in range(len(nums2)):
            if nums2[i]*nums2[i] in s1:
                ans += s1[nums2[i]*nums2[i]]

        return ans
