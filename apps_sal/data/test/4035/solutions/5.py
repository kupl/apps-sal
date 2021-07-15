from math import ceil

A,B = map(int,input().split())

min8 = ceil(A*12.5)
max8 = int((A+1)*12.5-0.001)
min10 = ceil(B*10)
max10 = int((B+1)*10-0.001)
#print(min8,max8,min10,max10)

if max8<min10 or max10<min8:
    print(-1)
else:
    print(max(min8,min10))
