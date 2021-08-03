class Solution:

    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        import functools
#         s_nums = []
#         maximum_length = 0
#         result = ""
#         dic = {}
#         for i in range(0, len(nums)):
#             value = str(num[i])
#             maximum_length = max(maximum_length, len(value))
#             s_nums.append(value)
#             dic[i] = True

#         for i in range(0, maximum_length-1):
#             temp_max = ""
#             temp_max_array = []
#             for j in range(0, s_nums-1):
#                 try:
#                     a = s_nums[j][i]
#                     try:
#                         b = s_nums[j][i+1]
#                     except:
#                         if dic[j] != False:
#                             temp_max_array.append(nums[j])
#                             dic[j] = False
#                         dic[j] += 1
#                 except:
#                     continue
#             print(temp_max_array)
#             result += ''.join(sorted(temp_max_array))

#         return result
        nums_str = []
        for each in nums:
            nums_str.append(str(each))

        result = ''.join(sorted(nums_str, key=functools.cmp_to_key(self.comparator)))

        if int(result) == 0:
            return '0'
        else:
            return result

    def comparator(self, a, b):

        num1 = a + b
        num2 = b + a

        if num1 > num2:
            return -1
        elif num2 > num1:
            return 1
        else:
            return 0
