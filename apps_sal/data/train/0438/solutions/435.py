class Solution:
   def findLatestStep(self, A, m):
        starts ={}
        ends ={}
        res = -1
        count = 0
        for i, a in enumerate(A):
            if a-1 in ends and a+1 in starts:
                end = starts.pop(a+1,None)
                if (end - (a+1) +1) == m: count-=1
                    
                st = ends.pop(a-1,None)
                if ((a-1)-st+1)==m: count-=1
                
                starts[st] = end
                ends[end] = st
                if(end-st+1) ==m: count+=1
                
            elif a-1 in ends:
                st = ends.pop(a-1, None)
                if ((a-1)-st+1)==m: count-=1
                    
                if a-1 in starts:
                    starts.pop(a-1,None)
                    
                ends[a]=st
                starts[st]=a
                if(a-st+1) ==m: count+=1
                
            elif a+1 in starts:
                end = starts.pop(a+1, None)
                if (end - (a+1) +1) == m: count-=1
                
                if a+1 in ends:
                    ends.pop(a+1,None)
                    
                starts[a]=end
                ends[end]=a
                if(end -a +1) ==m: count+=1
            else:
                ends[a]=a
                starts[a]=a
                if m ==1: count+=1
            if count: res = i+1    
        return res

