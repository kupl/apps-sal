class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        def c(nums1, nums2):
            ans = 0
            for num in nums1:
                count = defaultdict(int)

                for i in range(len(nums2)):
                    if nums2[i] in count:
                        ans += count[nums2[i]]

                    new = num*num
                    if new % nums2[i] == 0:
                        count[new//nums2[i]] += 1

            return ans

        ans = c(nums1, nums2) + c(nums2, nums1)
        return ans
