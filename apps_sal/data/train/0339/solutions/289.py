class Solution:

    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        num1_dict = collections.defaultdict(int)
        num2_dict = collections.defaultdict(int)
        for num in nums1:
            num1_dict[num] += 1
        for num in nums2:
            num2_dict[num] += 1
        res = 0
        for num in num1_dict:
            double = num ** 2
            for num2 in num2_dict:
                if double % num2 == 0 and double // num2 in num2_dict:
                    if num2 == double // num2:
                        res += num2_dict[num2] * (num2_dict[num2] - 1) * num1_dict[num]
                    else:
                        res += num2_dict[num2] * num2_dict[double // num2] * num1_dict[num]
        for num in num2_dict:
            double = num ** 2
            for num2 in num1_dict:
                if double % num2 == 0 and double // num2 in num1_dict:
                    if num2 == double // num2:
                        res += num1_dict[num2] * (num1_dict[num2] - 1) * num2_dict[num]
                    else:
                        res += num1_dict[num2] * num1_dict[double // num2] * num2_dict[num]
        return res // 2
