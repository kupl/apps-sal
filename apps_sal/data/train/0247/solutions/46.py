class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        
        left_sub_array = [len(arr)]*len(arr)
        
        sub_sum, next_index = 0, 0
        
        for index in range(len(arr)):
            
            while sub_sum < target and next_index < len(arr):
                sub_sum += arr[next_index]
                
                if sub_sum > target:
                    sub_sum -= arr[next_index]
                    break
                else:
                    if sub_sum == target :
                        left_sub_array[next_index] = (next_index - index) + 1                        
                    next_index += 1

                    
            sub_sum -= arr[index]
            
            left_sub_array[index] = min(left_sub_array[index], left_sub_array[index - 1])
        
        
        r_arr = arr[::-1]
        
        right_sub_array = [len(r_arr)]*len(r_arr)
        
        sub_sum, next_index = 0, 0
        
        for index in range(len(r_arr)):
            
            while sub_sum < target and next_index < len(r_arr):
                
                sub_sum += r_arr[next_index]
                                
                if sub_sum > target:
                    sub_sum -= r_arr[next_index]
                    break
                else:
                    if sub_sum == target :
                        right_sub_array[next_index] = (next_index - index) + 1
                    next_index += 1
                    
            sub_sum -= r_arr[index]
            right_sub_array[index] = min(right_sub_array[index], right_sub_array[index - 1])
        
        right_sub_array = right_sub_array[::-1]
        
        min_length = 2*len(arr)
        
        # print(left_sub_array, right_sub_array)
        
        for index, val in enumerate(left_sub_array[:-1]):
            
            min_length = min(min_length, val + right_sub_array[index + 1])
        
        
        if min_length > len(arr):
            return -1 
        else:
            return min_length
            
            
        
        
        

