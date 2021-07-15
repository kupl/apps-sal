# union find idea. But no need to implement union find, since only two sides can extend
class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        count_m = 0
        n = len(arr)
        string = [0]*(n+1)
        res = -1
        step = 0
        for loc in arr:
            step += 1
            l,r = loc,loc
            string[loc] = loc
            if(loc-1>=0 and string[loc-1]!=0):
                # merge with left
                if((loc-1)-string[loc-1]+1==m):  # one sequence with length m disapper
                    count_m -= 1
                    
                string[r]= l = string[loc-1]
                string[l] = r 
            if(loc+1<=n and string[loc+1]!=0):
                # merge with right
                if(string[loc+1]-(loc+1)+1==m):  # one sequence with length m disapper
                    count_m -= 1
                
                string[l] = r = string[loc+1]
                string[r] = l 
            
            if(r-l+1==m):
                count_m += 1
            if(count_m>0):
                res = step
            #print(string)
        
        return res
