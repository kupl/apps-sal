import math
x, y = map(int, input().split())
t = int(input())
min1 = 100000000
for i in range(t):
    a, b, c = map(int, input().split())
    # print(a,b,x,y,c)
    k = math.sqrt((x - a) * (x - a) + (y - b) * (y - b)) / c
    # rint(k)
    if(min1 > k):
        min1 = k
print(min1)
