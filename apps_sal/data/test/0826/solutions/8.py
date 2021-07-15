n=int(input())
import math
k=int((math.sqrt(8*n+9)-1)/2)
if n>=10000:
    for i in range(k-100,k+100):
        if i**2+i>2*(n+1):
            k=i-1
            break
print(n+1-k)
