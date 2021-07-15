import math
n=int(input())
k=0
l=int(math.sqrt(n-1))
for i in range(1,l+1):
    k+=(n-1)//i-i
print(k*2+l)
