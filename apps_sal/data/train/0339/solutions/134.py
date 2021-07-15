class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        ans = 0
        n1 = defaultdict(int)
        for n in nums1:
            n1[n] += 1
        n2 = defaultdict(int)
        for n in nums2:
            n2[n] += 1
        for j in range(len(nums1)):
            for k in range(j+1, len(nums1)):
                prod = nums1[j]*nums1[k]
                ans += n2[prod**0.5]
        for j in range(len(nums2)):
            for k in range(j+1, len(nums2)):
                prod = nums2[j]*nums2[k]
                ans += n1[prod**0.5]
        return ans

