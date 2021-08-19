class Solution:

    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        ret = 0
        (m, n) = (len(nums1), len(nums2))
        (_map1, _map2) = (Counter(nums1), Counter(nums2))
        for i in range(m):
            nums2_map = {**_map2}
            for j in range(n):
                nums2_map[nums2[j]] -= 1
                target = nums1[i] * nums1[i] / nums2[j]
                if nums2_map.get(target, 0) > 0:
                    ret += nums2_map.get(target, 0)
        for i in range(n):
            nums1_map = {**_map1}
            for j in range(m):
                nums1_map[nums1[j]] -= 1
                target = nums2[i] * nums2[i] / nums1[j]
                if nums1_map.get(target, 0) > 0:
                    ret += nums1_map.get(target, 0)
        return ret
