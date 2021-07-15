class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        # 1. Iterate i: 0 ~ n-2
        #   1a. find min length to make target number in 0 ~ i
        #   1b. if found, see if possible to make target number with consequent numbers starting from i+1
        #   1c. if found, update min
        
        n = len(arr)
        best_to = [n + 1 for _ in range(n)]
        best_from = dict()
        min_total = n + 1 # Naturally impossible length. Will be updated if any possible case exist. Will tell when no possible case
        min_left = n + 1
        sum_left = 0
        s_left = 0
        e_left = 0
        
        for i in range(n):
            sum_left += arr[i]
            if sum_left == target:
                best_to[i] = i - s_left + 1
                best_from[s_left] = i - s_left + 1
            elif sum_left > target:
                while s_left < i and sum_left > target:
                    sum_left -= arr[s_left]
                    s_left += 1
                if sum_left == target:
                    best_to[i] = i - s_left + 1
                    best_from[s_left] = i - s_left + 1
        
        for i in range(1, n):
            best_to[i] = min(best_to[i], best_to[i-1])
        
        for i in range(n - 1):
            if best_to[i] > n:
                continue
            
            if i + 1 in best_from:
                min_total = min(min_total, best_to[i] + best_from[i + 1])
        
#         for i in range(n - 1):
#             sum_left += arr[i]
#             if sum_left == target:
#                 # print(str(s_left) + '->' + str(e_left))
#                 best[s_left] = e_left - s_left + 1
#                 min_left = min(min_left, best[s_left])
#             elif sum_left > target:
#                 # Need to drop some numbers
#                 while s_left < e_left and sum_left > target:
#                     sum_left -= arr[s_left]
#                     s_left += 1
#                 if sum_left == target:
#                     min_left = min(min_left, e_left - s_left + 1)
#             # Skip if a subarray is not found on left
#             if min_left > n:
#                 continue
            
#             if i + 1 in 
#             sum_right = 0
#             for j in range(i + 1, n):
#                 sum_right += arr[j]
#                 if sum_right == target:
#                     min_total = min(min_total, min_left + j - i)
#                 elif sum_right > target:
#                     # Stop following as already exceeded
#                     break
        
        if min_total > n:
            return -1
        
        return min_total

