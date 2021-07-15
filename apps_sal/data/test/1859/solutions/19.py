import math
def primeFactors(n): 
    if(n%2==0):
        return 2   
    for i in range(3,int(math.sqrt(n))+1,2): 
        if(n % i== 0): 
            return i 
    if(n > 2): 
        return n 
           
n=int(input())
k=primeFactors(n)
if(k==2):
    print(n//k)
elif(k==n):
    print(1)
else:
    n-=k
    print(1+(n//2))
