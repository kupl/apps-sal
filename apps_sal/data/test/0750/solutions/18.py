import math
n,k  =[*list(map(int, input().split()))]

count = 0

count+= math.ceil(2*n/k)
count+= math.ceil(5*n/k)
count+= math.ceil(8*n/k)
print(count)


