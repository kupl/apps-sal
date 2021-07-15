class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        bit_information = [0] * (len(arr) + 1)
        target_group_size_counter = 0
        ret = -2
        
        
        for i in range(len(arr)):
            group_sizes = []
            total_length = None
            
            
            if (arr[i] > 1 and bit_information[arr[i] - 1] != 0 and arr[i] < len(arr) and bit_information[arr[i] + 1] != 0):
                group_sizes = [bit_information[arr[i] - 1], bit_information[arr[i] + 1]]
                total_length = 1 + bit_information[arr[i] - 1] + bit_information[arr[i] + 1]
                bit_information[arr[i] - bit_information[arr[i] - 1]] = total_length
                bit_information[arr[i] + bit_information[arr[i] + 1]] = total_length
            elif (arr[i] > 1 and bit_information[arr[i] - 1] != 0):
                group_sizes = [bit_information[arr[i] - 1]]
                total_length = bit_information[arr[i] - 1] + 1
                bit_information[arr[i] - bit_information[arr[i] - 1]] = total_length
                bit_information[arr[i]] = total_length
            elif (arr[i] < len(arr) and bit_information[arr[i] + 1] != 0):
                group_sizes = [bit_information[arr[i] + 1]]
                total_length = bit_information[arr[i] + 1] + 1
                bit_information[arr[i] + bit_information[arr[i] + 1]] = total_length
                bit_information[arr[i]] = total_length
            else:
                bit_information[arr[i]] = 1
                total_length = 1
                
            target_group_size_counter -= group_sizes.count(m)
            target_group_size_counter += 1 if total_length == m else 0
            

            if (target_group_size_counter > 0):
                ret = i
                
        return ret + 1       
