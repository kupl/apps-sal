class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        
        left_min = self.getMinArr(arr, target, True)
        right_min = self.getMinArr(arr, target, False)
        
        result = sys.maxsize
        for i in range(0, len(arr)-1):
            if max(left_min[i], right_min[i+1]) != sys.maxsize:
                result = min(left_min[i] + right_min[i+1], result)
        
        return result if result < sys.maxsize else -1
    
    def getMinArr(self, arr, target, right):
        result = [sys.maxsize] * len(arr)
        current_sum = 0
        num_map = {0: 0}
        
        nums = arr if right else arr[::-1]
        for i, num in enumerate(nums):
            if i > 0:
                result[i] = result[i-1]
            current_sum += num
            
            if current_sum - target in num_map:
                current_len = i - num_map[current_sum-target] + 1
                result[i] = min(result[i], current_len)
            
            num_map[current_sum] = i+1
        
        if not right:
            result.reverse()
        
        return result

