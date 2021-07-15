import math
c,d=list(map(int,input('').split()))
n,m=list(map(int,input('').split()))
k=int(input(''))
if n*m-k<0:
    print('0')
    return
if 1/d>n/c:    print((n*m-k)*d)
else:
    if (math.ceil((n*m-k)/n)*c)<((n*m-k)//n)*c+((n*m-k)%n)*d: print(math.ceil((n*m-k)/n)*c)
    else: print(((n*m-k)//n)*c+((n*m-k)%n)*d)







            
            
        
        
    


                


