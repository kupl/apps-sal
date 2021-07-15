import math
temp = input().split(' ')
n = int(temp[0])
x = int(temp[1])
t = int(temp[2])
num = n/x
ans = math.ceil(num) * t
print(ans)
