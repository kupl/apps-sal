class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        cnt = 0
        for num in nums1:
            target = num * num
            cnt += self.twoProduct(nums2, target)

        for num2 in nums2:
            target2 = num2 * num2
            cnt += self.twoProduct(nums1, target2)

        return cnt

    def twoProduct(self, nums, target):
        cnt = 0
        hashmap = collections.defaultdict(int)
        for i in range(len(nums)):
            if target / nums[i] in hashmap:
                cnt += hashmap[target / nums[i]]
            hashmap[nums[i]] += 1

        return cnt
