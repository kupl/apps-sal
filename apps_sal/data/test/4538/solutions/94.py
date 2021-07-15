import math
 
temp = list(map(int,input().split()))
count = 0
 
for i in range(temp[0]):
  l = list(map(int,input().split()))
  if(math.sqrt(l[0]*l[0]+l[1]*l[1])<=temp[1]):
    count += 1
print(count)
