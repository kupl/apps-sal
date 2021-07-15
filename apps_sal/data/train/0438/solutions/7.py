class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        if (m == len(arr)):
            return len(arr)
        
        bit_information = [0] * (len(arr) + 2)
        target_group_size_counter = 0
        ret = -2
        
        
        for i in range(len(arr)):
            total_length = 1 + bit_information[arr[i] - 1] + bit_information[arr[i] + 1]   
            bit_information[arr[i]] = total_length
            target_group_size_counter -= 1 if bit_information[arr[i] - 1] == m else 0
            bit_information[arr[i] - bit_information[arr[i] - 1]] = total_length
            target_group_size_counter -= 1 if bit_information[arr[i] + 1] == m else 0
            bit_information[arr[i] + bit_information[arr[i] + 1]] = total_length
            target_group_size_counter += 1 if total_length == m else 0
            ret = i if target_group_size_counter > 0 else ret
            
        return ret + 1       
