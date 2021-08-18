class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        INF = len(arr) + 1
        best_idx = [INF] * len(arr)
        best = INF
        csum = 0

        left = 0
        for right in range(len(arr)):
            csum += arr[right]

            while csum > target and left <= right:
                csum -= arr[left]
                left += 1

            if csum == target:
                best = min(best, best_idx[left - 1] + right - left + 1)
                best_idx[right] = min(best_idx[right - 1], right - left + 1)
            else:
                best_idx[right] = best_idx[right - 1]

        if INF == best:
            return -1
        return best


'''
class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        INF = len(arr) + 1
        best_at_i = [INF]*len(arr) 
        best = INF 
        curr_sum = 0 
        
        left = 0
        for right in range(len(arr)):
            curr_sum += arr[right]
            
            while curr_sum > target and left <= right:
                curr_sum -= arr[left]
                left += 1
                
            if curr_sum == target:
                best = min(best, best_at_i[left-1] + right - left + 1)
                best_at_i[right] = min(best_at_i[right-1], right - left + 1)
            else:
                best_at_i[right] = best_at_i[right-1]

        if best == INF:
            return -1
        return best'''
