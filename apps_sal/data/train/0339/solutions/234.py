class Solution:

    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)
        count = 0
        for item in nums1:
            count += self.get_equal_square(item * item, nums2)
        for item in nums2:
            count += self.get_equal_square(item * item, nums1)
        return count

    def get_equal_square(self, val, arr):
        count = 0
        m = {}
        for (i, item) in enumerate(arr):
            if val % item:
                continue
            tmp = val / item
            if m.get(tmp, None):
                count += m.get(tmp)
            m[item] = m.get(item, 0) + 1
        return count
