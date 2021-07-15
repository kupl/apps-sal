class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        
        sums_list = [0]
        sums_dict ={0:0}
    
        s=0
        for i in range(len(arr)):
            s += arr[i]
            sums_dict[s] = i + 1
            sums_list.append(s)

            
        lengths = [0]*len(sums_list)
        min_length = float('+inf')
        for start in range(len(sums_list) - 1, -1, -1):
            #s[end] - s[start] = target
            val = sums_list[start] + target
            if val in sums_dict:
                end = sums_dict[val]
                min_length = min(min_length, end - start)
            lengths[start] = min_length
        
        min_length = float('+inf')
        for start in range(len(sums_list)):
            val = sums_list[start] + target
            if val in sums_dict:
                end = sums_dict[val]

                l = end - start + lengths[end]
                min_length = min(min_length, l)
        if min_length != float('+inf'):
            return min_length
        else:
            return -1
        
            
        
        
            

