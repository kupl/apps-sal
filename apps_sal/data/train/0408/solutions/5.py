# class Solution(object):
#     def getRes(self,arr,t):
#         nums = [t if num >= t else num for num in arr]
#         return sum(nums)

#     def findBestValue(self, arr, target):
#         \"\"\"
#         :type arr: List[int]
#         :type target: int
#         :rtype: int
#         \"\"\"
#         l = 1
#         h = max(arr)

#         while l <= h:
#             mid = (h-l)//2 + l
#             curr = self.getRes(arr,mid)
#             if curr == target:
#                 return mid
#             elif curr < target:
#                 l = mid+1
#             else:
#                 h = mid-1
#         if abs(self.getRes(arr,l) - target) < abs(self.getRes(arr,h) - target):
#             return l
#         return h

class Solution:
    def score(self, value):
        res = 0
        for e in self.arr:
            if e > value:
                res += value
            else:
                res += e
        return res

    def findBestValue(self, arr: List[int], target: int) -> int:
        self.arr = arr[:]
        l, h = 1, max(arr)
        while l < h:
            m = (l + h) // 2
            if self.score(m) < target:
                l = m + 1
            else:
                h = m
        #print(l, h)
        s1 = abs(self.score(h - 1) - target)
        s2 = abs(self.score(h) - target)
        if s1 <= s2:
            return h - 1
        return h


# class Solution:
#     def findBestValue(self, arr: List[int], target: int) -> int:
#         #int arr
#         #target is what I want
#         #Return value

#         #WANT -> Return the value s.t
# #Constraint -> CHANGE all integers > value in the array to be EQUAL to value.
# #Get the sum of the array as CLOSE (abs diff) as possible to the target


# #In case of tie return the min int

#         def mutated_sum(left, right, target, value):
#             # abs_diff = 0
#             cur_sum = 0
#             for num in arr:
#                 if num >= value:
#                     cur_sum += value
#                 elif num < value:
#                     cur_sum += num


#              #abs_diff is 1
#             return cur_sum
#         #[4, 9, 3] target = 10
#         left = 1
#         right = max(arr)
#         min_diff = target
#         prev_min_val = right

#         #left = 3
#         #right = 4
#         while left < right:
#             value = left + (right - left) // 2
#             cur_sum = mutated_sum(left, right, target, value)
#             if cur_sum == target:
#                 return value
#             curr_diff = abs(target - cur_sum)

#             if curr_diff < min_diff:
#                 min_diff = curr_diff
#                 prev_min_val = value
#             elif curr_diff == min_diff:
#                 prev_min_val = min(prev_min_val, value)
#             if cur_sum <= target: #IF MY CUR_SUM is < target
#                 #THE MORE I MOVE LEFT the farther I am far from target
#                 # min_diff = cur_diff #min_diff is 1
#                 left = value

#             else: #cur_sum >= target
#                 right = value - 1

#         if abs(mutated_sum(left,right, target,left) - target) < \\
#         abs(mutated_sum(left,right, target,right)) - target:
#             return left

#         return right
