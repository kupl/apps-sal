import math
    

# int(input())
# [int(i) for i in input().split()]

n = int(input())
a = [int(i) for i in input().split()]

ans = -10000000

for x in a:
    if x < 0:
        if  x > ans: ans = x
        continue
    if int(math.sqrt(x))*int(math.sqrt(x)) != x and x > ans:
        ans = x

print(ans)

