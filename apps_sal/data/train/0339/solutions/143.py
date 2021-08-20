class Solution:

    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        count1 = collections.Counter(nums1)
        count2 = collections.Counter(nums2)
        result = 0
        for num1 in count1:
            for num2 in count2:
                if num1 ** 2 % num2 == 0 and num1 ** 2 // num2 in count2:
                    target = num1 ** 2 // num2
                    if target == num2:
                        if count2[num2] > 1:
                            result += count1[num1] * (count2[num2] * (count2[num2] - 1) // 2)
                    else:
                        result += count1[num1] * (count2[num2] * count2[target] / 2)
        for num2 in count2:
            for num1 in count1:
                if num2 ** 2 % num1 == 0 and num2 ** 2 // num1 in count1:
                    target = num2 ** 2 // num1
                    if target == num1:
                        if count1[num1] > 1:
                            result += count2[num2] * (count1[num1] * (count1[num1] - 1) // 2)
                    else:
                        result += count2[num2] * (count1[num1] * count1[target] / 2)
        return int(result)
