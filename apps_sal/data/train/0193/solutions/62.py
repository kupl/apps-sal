class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        
        dict_freq = {}
        
        for i in range(len(arr)):
            if arr[i] in dict_freq:
                dict_freq[arr[i]] += 1
            else:
                dict_freq[arr[i]] = 1
                
        target_size = len(arr)//2
        sort_dict = dict(sorted(list(dict_freq.items()), key=lambda x: x[1], reverse=True))
        print(sort_dict)
        for i in dict_freq:
            
            if dict_freq[i] >= target_size:
                
                return 1
            else:
                break
        cnt = 0 
        count = 0
        for i in sort_dict:
            cnt = cnt + sort_dict[i]
            count = count+1
            if cnt >= target_size:
                return count
                
        return 8
            
            

