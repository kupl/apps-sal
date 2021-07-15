
import math
from collections import *
a=int(input())
indx=defaultdict(list)
done=defaultdict(list)
for t in range(a):
    s=input()
    for i in range(len(s)):
        for j in range(i,len(s)):
            m=s[i:j+1]
            
            if(len(done[m])==0):
                done[m].append(t)
                indx[t].append(m)
            else:
                if(len(done[m])==1 and  done[m][0]!=math.inf and t!=done[m][0]):
                    indx[done[m][0]].remove(m)
                    done[m][0]=math.inf
            
 
for i in range(a):
    af=indx[i]
 
    mini=15
    ss=''
    for i in range(len(af)):
        if(len(af[i])<mini):
            mini=len(af[i])
            ss=af[i]
    print(ss)
        


        
        

