class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort()
        ans = 0
        for i in range(len(nums1)):
            h1 = {}
            target = nums1[i] * nums1[i]
            for j in range(len(nums2)):
                if target/nums2[j] in h1:
                    ans += h1[target/nums2[j]]
                if nums2[j] in h1:
                    h1[nums2[j]] += 1
                else:
                    h1[nums2[j]] = 1
                
                
        for i in range(len(nums2)):
            h2 = {}
            target = nums2[i] * nums2[i]
            for j in range(len(nums1)):
                if target/nums1[j] in h2:
                    ans += h2[target/nums1[j]]
                if nums1[j] in h2:
                    h2[nums1[j]] += 1
                else:
                    h2[nums1[j]] = 1        

        return ans
