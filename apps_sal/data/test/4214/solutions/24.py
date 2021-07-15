from itertools import permutations
import math
n = int(input())
x,y = [],[]
for _ in range(n):
    x_, y_ =map(int,input().split())
    x.append(x_)
    y.append(y_)
c = list(permutations([i for i in range(1,n+1)],n))
sum = 0
for ci in (c):
    tmp = 0
    for i in range(len(ci)-1):
            tmp += math.sqrt((x[ci[i]-1]-x[ci[i+1]-1])**2 
                             + (y[ci[i]-1]-y[ci[i+1]-1])**2)
    sum += tmp
print(sum/len(c))
