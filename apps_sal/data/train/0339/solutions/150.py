class Solution:

    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort()
        count = 0
        nums1m = [x * x for x in nums1]
        nums2m = [x * x for x in nums2]
        d1 = defaultdict(int)
        d2 = defaultdict(int)
        for num in nums1:
            d1[num] += 1
        for num in nums2:
            d2[num] += 1
        for num in nums1m:
            for j in range(len(nums2)):
                if nums2[j] > num:
                    break
                if num % nums2[j] != 0:
                    continue
                left = num // nums2[j]
                if left in d2:
                    if left == nums2[j]:
                        count += d2[left] - 1
                    else:
                        count += d2[left]
        for num in nums2m:
            for j in range(len(nums1)):
                if nums1[j] > num:
                    break
                if num % nums1[j] != 0:
                    continue
                left = num // nums1[j]
                if left in d1:
                    if left == nums1[j]:
                        count += d1[left] - 1
                    else:
                        count += d1[left]
        return count // 2
