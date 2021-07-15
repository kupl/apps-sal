class Solution:
    def find(self, nums, target):
        seen = collections.defaultdict(int)
        res = 0
        for i in nums:
            if target % i == 0 and target/i in seen:
                res += seen[target/i]
            seen[i] += 1
        return res
        
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        res = 0
        for i in nums1:
            target = i * i
            res += self.find(nums2, target)
        for i in nums2:
            target = i * i
            res += self.find(nums1, target)
        return res
