class Solution:

    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        count = 0
        for i in range(len(nums1)):
            target = nums1[i] ** 2
            temp = defaultdict(int)
            for j in range(len(nums2)):
                if target / nums2[j] in list(temp.keys()):
                    count += temp[target / nums2[j]]
                temp[nums2[j]] += 1
        for i in range(len(nums2)):
            target = nums2[i] ** 2
            temp = defaultdict(int)
            for j in range(len(nums1)):
                if target / nums1[j] in list(temp.keys()):
                    count += temp[target / nums1[j]]
                temp[nums1[j]] += 1
        return count
