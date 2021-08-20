class Solution:

    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:

        def helper(target, nums):
            dic = collections.defaultdict(int)
            count = 0
            for num in nums:
                if target % num == 0 and target // num in dic:
                    count += dic[target // num]
                dic[num] += 1
            return count
        ans = 0
        for x in nums1:
            ans += helper(x ** 2, nums2)
        for x in nums2:
            ans += helper(x ** 2, nums1)
        return ans
