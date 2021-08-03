class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        count = self.findTriple(nums1, nums2)
        count += self.findTriple(nums2, nums1)

        return count

    def findTriple(self, nums1, nums2):
        counts = {}
        for num in nums2:
            if num not in counts:
                counts[num] = 0
            counts[num] += 1

        tcount = 0
        for i in range(0, len(nums1)):
            for j in range(0, len(nums2)):
                if nums2[j] < nums1[i] and (nums1[i] * nums1[i]) % nums2[j] == 0 and (nums1[i] * nums1[i]) // nums2[j] in counts:
                    tcount += counts[nums1[i] * nums1[i] // nums2[j]]

            if nums1[i] in counts:
                tcount += (counts[nums1[i]] * (counts[nums1[i]] - 1) // 2)

        return tcount
