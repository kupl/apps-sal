import math
n=int(input())
a=[]
for i in range(5):
    a.append(int(input()))

print(4+math.ceil(n/min(a)))
