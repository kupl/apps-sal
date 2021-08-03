class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
        import math
        curr_gcd = nums[0]
        for i in range(1, len(nums)):
            curr_gcd = math.gcd(curr_gcd, nums[i])
            if curr_gcd == 1:
                return True
        return curr_gcd == 1

        # if 1 in nums: return True

#         def find_factors(num):
#             sol = set()
#             for i in range(1,math.ceil(math.sqrt(num))):
#                 if num % i == 0:
#                     sol.add(i)
#                     sol.add(num/i)
#             # sol.remove(num)
#             sol.remove(1)
#             return sol

#         all_items = set()
#         factors_list = []
#         for num in nums:
#             temp_set = find_factors(num)
#             for it in temp_set:
#                 all_items.add(it)

#             factors_list.append(temp_set)
#         # print(all_items)
#         # print(factors_list)
#         for it in all_items:
#             if it == 1: continue
#             if all([it in lis for lis in factors_list]):
#                 return False

#         return True

        '''
        29, 6, 10
        29, 3*2, 5*2
        '''
