def check(arr, mid, D):
    count = 1
    n = len(arr)
    cur_sum = 0
    for i in range(n):
        if cur_sum + arr[i] > mid:
            count += 1
            cur_sum = 0
        cur_sum += arr[i]
        if count > D:
            return False
    
    return count <= D


class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        
        max_weight = sum(weights)
        min_weight = max(weights)
        ans = float('inf')
        
        while min_weight <= max_weight:
            mid = int((max_weight + min_weight)/2)
            if check(weights, mid, D) == True:
                ans = min(ans, mid)
                max_weight = mid - 1
            else:
                min_weight = mid + 1
        
        return ans

