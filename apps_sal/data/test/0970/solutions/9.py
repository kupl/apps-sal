import math
n = int(input())
cnt0 = 0
cnt1 = 0
p = input().split()
for i in range(n//2):
    p[i] = int(p[i])-1
p.sort()
for i in range(n//2):
    cnt0+=math.fabs(p[i]-2*i)
    cnt1+=math.fabs(p[i] - 2*i-1)
print(int(min(cnt0,cnt1)))    

            
        
    
    
    
    
        
    
    
    

    
    
   


