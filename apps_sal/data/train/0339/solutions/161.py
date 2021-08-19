class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        def twoProduct(target, nums):
            cnt = 0
            currMap = collections.defaultdict(lambda: 0)

            for num in nums:
                # 如果 target 整除 num2，且 target // num2 在 map 中，那么结果加上 map 中 target // num2 的个数
                if target % num == 0 and target // num in currMap:
                    cnt += currMap[target // num]

                currMap[num] += 1

            return cnt

        res = 0

        # 对于每一个 nums1 中的数，都创建一个 map
        for num1 in nums1:
            target = num1 * num1
            res += twoProduct(target, nums2)

        for num2 in nums2:
            target = num2 * num2
            res += twoProduct(target, nums1)

        return res
