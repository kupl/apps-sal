from collections import deque


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        step = 0
        while sum(nums):
            for i, val in enumerate(nums):
                if val % 2:
                    nums[i] -= 1
                    step += 1
            if sum(nums):
                step += 1
                for i, val in enumerate(nums):
                    if val:
                        nums[i] /= 2
        return step


#         step = 0
#         l = deque()
#         l.append([0] * len(nums))
#         while l:
#             l_len = len(l)
#             for i in range(l_len):
#                 cur_list = l.popleft()
#                 if str(cur_list) == str(nums):
#                     return step
#                 for j in range(len(nums)):
#                     add_next, valid = self.add(cur_list, nums, j)
#                     if valid:
#                         l.append(add_next)
#                 mul_next, valid = self.multiply(cur_list, nums)
#                 if valid:
#                     l.append(mul_next)
#             step += 1
#         return step


#     def add(self, cur: List[int], target: List[int], idx: int):
#         if cur[idx] + 1 > target[idx]:
#             return [], False
#         else:
#             new_list = cur.copy()
#             new_list[idx] += 1
#             return new_list, True

#     def multiply(self, cur: List[int], target: List[int]):
#         new_list = cur.copy()
#         for i in range(len(new_list)):
#             new_list[i] *= 2
#             if new_list[i] > target[i]:
#                 return [], False
#         return new_list, True
