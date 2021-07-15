import math 
n,s=list(map(int,input('').split()))
L=[]
for i in range(n):
    x,y,z=list(map(int,input('').split()))
    L+=[(math.sqrt(x*x+y*y),z)]
L.sort()
count=s
if s>=1000000:
    print('0')
    return
for i in L:
    count+=i[1]
    if count>=1000000:
        print(i[0])
        return
    
print('-1')





            
            
        
        
    


                


