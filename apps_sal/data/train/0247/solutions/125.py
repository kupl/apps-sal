class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        best_so_far = [float('inf') for i in range(len(arr)+1)]
        prefix_sum = 0
        prefix_sum_to_idx = {0:-1}
        res = float('inf')
        for i,v in enumerate(arr):
            prefix_sum += v
            best_so_far[i+1] = best_so_far[i]
            prev_sum = prefix_sum - target
            if prev_sum in prefix_sum_to_idx:
                res = min(res, best_so_far[prefix_sum_to_idx[prev_sum]+1] + i - prefix_sum_to_idx[prev_sum])
                best_so_far[i+1] = min(best_so_far[i], i - prefix_sum_to_idx[prev_sum])
            prefix_sum_to_idx[prefix_sum] = i
        return -1 if res == float('inf') else res 

