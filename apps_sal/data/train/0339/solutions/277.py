class Solution:

    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        from collections import defaultdict
        count = 0
        Dict = defaultdict(int)
        for i in range(len(nums1)):
            num = nums1[i] * nums1[i]
            Dict.clear()
            for j in range(len(nums2)):
                if Dict[nums2[j]] > 0:
                    count += Dict[nums2[j]]
                if num % nums2[j] == 0:
                    x = num // nums2[j]
                    Dict[x] += 1
        Dict.clear()
        for i in range(len(nums2)):
            num = nums2[i] * nums2[i]
            Dict.clear()
            for j in range(len(nums1)):
                if Dict[nums1[j]] > 0:
                    count += Dict[nums1[j]]
                if num % nums1[j] == 0:
                    x = num // nums1[j]
                    Dict[x] += 1
        return count
