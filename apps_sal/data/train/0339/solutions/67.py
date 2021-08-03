class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        rep = 0
        rep += self.getNumTriplets(nums1, nums2)
        rep += self.getNumTriplets(nums2, nums1)
        return rep

    def getNumTriplets(self, nums1, nums2):
        num1 = [n**2 for n in nums1]
        num2 = []
        for i in range(len(nums2) - 1):
            for j in range(i + 1, len(nums2)):
                num2.append(nums2[i] * nums2[j])
        num2.sort()
        num1.sort()

        rep = 0
        k = 0
        while k < len(num1):
            cur = self.exist(num2, num1[k])
            rep += cur
            while k + 1 < len(num1) and num1[k + 1] == num1[k]:
                rep += cur
                k += 1
            k += 1
        return rep

    def exist(self, nums, target):
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:  # nums[mid]==target
                l = self.leftSearch(nums[:mid + 1], target)
                r = self.rightSearch(nums[mid:], target) + mid
                return r - l + 1
        return 0

    def leftSearch(self, nums, target):
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                r = mid - 1
            else:
                l = mid + 1
        return l

    def rightSearch(self, nums, target):
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                l = mid + 1
            else:
                r = mid - 1
        return r
