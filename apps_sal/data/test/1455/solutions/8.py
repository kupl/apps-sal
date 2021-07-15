from math import ceil
n = int(input())
ans = ceil((n+1)/2)
print(ans)
x = y = 1
for i in range(n):
    print(x,y)
    if x != ans: x+=1
    else: y += 1

