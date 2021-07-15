class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        for i in range(1, len(arr)):
            arr[i] += arr[i-1]
        
        # arr is now prefix_sum
        
        index = {0: -1} # map prefix_sum -> index of that sum
        best_till = [float('inf')] * len(arr) # best_till[i] is best answer up till that
        res = float('inf')
        best = float('inf')
        
        for i,val in enumerate(arr):
            if val-target in index:
                start_of_window = index[val-target]
                length = i - start_of_window
                res = min(res, best_till[start_of_window+1] + length)
                best = min(best, length)
            if i+1 < len(best_till):
                best_till[i+1] = best
            index[val] = i
        
        return -1 if res == float('inf') else res
        
        
'''
target=7
[1,6,1]

arr=[1,7,8]
index { 0->-1, 1->0, }
best_till= [inf, 2, 2]
res = inf

i=2, val=8
start_of_window = 0
length = 2

'''
