class Solution:

    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        count = 0
        dic1 = dict()
        for num in nums1:
            if num in dic1:
                dic1[num] += 1
            else:
                dic1[num] = 1
        dic2 = dict()
        for num in nums2:
            if num in dic2:
                dic2[num] += 1
            else:
                dic2[num] = 1
        for num1 in nums1:
            square = num1 ** 2
            for num2 in nums2:
                if square / num2 in dic2:
                    if square / num2 == num2:
                        count += dic2[square / num2] - 1
                    else:
                        count += dic2[square / num2]
        for num2 in nums2:
            square = num2 ** 2
            for num1 in nums1:
                if square / num1 in dic1:
                    if square / num1 == num1:
                        count += dic1[square / num1] - 1
                    else:
                        count += dic1[square / num1]
        return int(count / 2)
