class Solution:

    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        res = 0
        for num1 in nums1:
            currMap = collections.defaultdict(lambda: 0)
            target = num1 * num1
            for num2 in nums2:
                if target % num2 == 0 and target // num2 in currMap:
                    res += currMap[target // num2]
                currMap[num2] += 1
        for num2 in nums2:
            currMap = collections.defaultdict(lambda: 0)
            target = num2 * num2
            for num1 in nums1:
                if target % num1 == 0 and target // num1 in currMap:
                    res += currMap[target // num1]
                currMap[num1] += 1
        return res
