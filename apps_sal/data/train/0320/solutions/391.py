class Solution:
    def minOperations(self, nums: List[int]) -> int:
        zeros = [0 for el in nums]
        res = 0
        while nums != zeros:
            for i in range(len(nums)):
                if nums[i] % 2 != 0:
                    nums[i] -= 1
                    res += 1
            if nums == zeros:
                break
            nums = [el / 2 for el in nums]
            res += 1
        return res


#         double_arr = [math.floor(math.log(num, 2)) for num in nums]
#         calc = [0 for el in nums]
#         zeros_arr = [0 for el in nums]
#         # iters = 0
#         res = 0
#         while True:
#             # Add 1s
#             print(\"~~~~~~~~~calc\", calc)
#             print(\"double arr\", double_arr)
#             max_idxs = []
#             max_val = 0
#             for idx, val in enumerate(double_arr):
#                 if val > max_val:
#                     max_val = val
#                     max_idxs = [idx]
#                 elif val == max_val:
#                     max_idxs.append(idx)
#             if max_val == 0: break
#             # print(\"max idxs\", max_idxs)
#             for idx in max_idxs:
#                 if calc[idx] == 0:
#                     calc[idx] += 1
#                     res += 1
#                 double_arr[idx] -= 1
#             # print(\"inter calc\", calc)
#             calc = [el*2 for el in calc]
#             # print(\"end calc\", calc)
#             res += 1
#             print(\"res\", res)
#             # if iters>50: break
#             # iters += 1

#         diff_remain = sum(nums) - sum(calc)
#         res += diff_remain
#         return res
