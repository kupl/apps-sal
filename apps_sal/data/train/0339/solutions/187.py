class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort()
        count = self.counttrip(nums1, nums2)

        count += self.counttrip(nums2, nums1)
        return int(count)

    def counttrip(self, nums1, nums2):

        count = 0
        for i in nums1:

            target = i * i
            dictn = defaultdict(int)
            for j, x in enumerate(nums2):
                rem = target / x
                if(rem in dictn):
                    count += dictn[rem]
                dictn[x] += 1
        return count
