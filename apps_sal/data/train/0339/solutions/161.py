class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        def twoProduct(target, nums):
            cnt = 0
            currMap = collections.defaultdict(lambda: 0)

            for num in nums:
                if target % num == 0 and target // num in currMap:
                    cnt += currMap[target // num]

                currMap[num] += 1

            return cnt

        res = 0

        for num1 in nums1:
            target = num1 * num1
            res += twoProduct(target, nums2)

        for num2 in nums2:
            target = num2 * num2
            res += twoProduct(target, nums1)

        return res
