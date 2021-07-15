class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        arr.sort()
        low = 0 
        high = (1 << 32)
        closest_diff = None
        closest_index = None
        while ((high - low) > 1):
            mid = (high + low) // 2
            mid_val = self.helper(arr,mid)
            if (closest_diff == None) or (closest_diff > abs(target - mid_val)):
                closest_index = mid
                closest_diff = abs(target - mid_val)
            elif (closest_diff == abs(target - mid_val) and mid < closest_index):
                closest_index = mid
                closest_diff = abs(target - mid_val)
                
            print(high,low,mid,self.helper(arr,mid),closest_index)

            if (mid_val < target) and (mid <= arr[len(arr) - 1]):
                low = mid
            else:
                high = mid
                
        high_val = self.helper(arr,high)
        if (closest_diff == None) or (closest_diff > abs(target - high_val)):
            closest_index = high
            closest_diff = abs(target - high_val)
        low_val = self.helper(arr,low)
        if (closest_diff == None) or (closest_diff > abs(target - low_val)):
            closest_index = low
            closest_diff = abs(target - low_val)
        elif (closest_diff == low_val and low < closest_index):
            closest_index = low
            closest_diff = abs(target - low_val)
        return closest_index
    
    def helper(self,arr,val):
        curr_sum = 0
        for num in arr:
            if num < val:
                curr_sum += num
            else:
                curr_sum += val
        return curr_sum
