from collections import defaultdict
class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        s_d = defaultdict(list)
        e_d = defaultdict(list)
        lengths = defaultdict(int)
        latest = -1
        step = 1
        for i in arr:
            
            end = i - 1
            start = i + 1
            
            if end in e_d and start in s_d:
                s_l = s_d[start]
                e_l = e_d[end]
                x = s_l[1] - s_l[0] + 1
                y = e_l[1] - e_l[0] + 1
                lengths[x] -= 1
                lengths[y] -= 1
                if lengths[x] == 0:
                    del lengths[x]
                if lengths[y] == 0:
                    del lengths[y]
                del s_d[start]
                del e_d[end]
                
                l = [e_l[0],s_l[1]]
                length = l[1] - l[0] + 1                
                
                lengths[length] += 1
                s_d[l[0]] = l 
                e_d[l[1]] = l
            elif end in e_d:
                e_l = e_d[end]
                x = e_l[1] - e_l[0] + 1 
                lengths[x] -= 1
                if lengths[x] == 0:
                    del lengths[x]
                    
                del e_d[end]
                
                e_l[1] = i 
                e_d[e_l[1]] = e_l
                length = e_l[1] - e_l[0] + 1
                lengths[length] += 1
                
            elif start in s_d:
                s_l = s_d[start]
                x = s_l[1] - s_l[0] + 1 
                lengths[x] -= 1 
                if lengths[x] == 0:
                    del lengths[x]
                    
                del s_d[start]
                s_l[0] = i 
                s_d[i] = s_l
                length = s_l[1] - s_l[0] + 1
                lengths[length] += 1
            else:
                
                l = [i,i]
                s_d[i] = l 
                e_d[i] = l 
                
                lengths[1] += 1
            # print(i,s_d,lengths)
            if m in lengths:
                latest = step
            step += 1
        return latest
                

