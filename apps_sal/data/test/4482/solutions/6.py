import math
n = int(input())
a = list(map(int,input().split()))
avg = sum(a)/n
x = math.floor(avg)
y = math.ceil(avg)
sumx = 0
sumy = 0
for i in a:
    sumx += (i - x) ** 2
    sumy += (i - y) ** 2

print(min([sumx,sumy]))
