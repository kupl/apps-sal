import math
n=int(input())-1
x = ((8*n+1)**0.5-1)//2
y=x*(x+1)/2
print(int(n-y+1))
