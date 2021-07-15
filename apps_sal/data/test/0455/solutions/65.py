def pow2(i):
    ret = 1
    while i!=1:
        i >>= 1
        ret <<= 1
    return ret

m = int(input())

points = []
max2 = -1
flag = True
bias = -1
for i in range(m):
    point = list(map(int,input().split()))
    dis = abs(point[0])+abs(point[1])
    if (dis > max2):
        max2 = dis
    if (bias!=-1 and dis%2 != bias%2):
        flag =False
    if (dis%2 == 0):
        point[0] -= 1 
    points.append(tuple(point))
    bias = dis%2
if flag == False:
    print("-1")
    return        

bias = max2%2
max2 = pow2(max2)
diss = []
dirctions = [""]*m
while max2>0:
    for i in range(m):
        point = points[i]
        
        if (point[1]>point[0] and point[1]>(-point[0])):
            dirctions[i] = "U"+dirctions[i]
            points[i] = (point[0],point[1]-max2)
        elif(point[1]>point[0] and point[1]<(-point[0])):
            dirctions[i] = "L"+dirctions[i]
            points[i] = (point[0]+max2,point[1])
        elif(point[1]<point[0] and point[1]>(-point[0])):
            dirctions[i] = "R"+dirctions[i]
            points[i] = (point[0]-max2,point[1])
        else:
            dirctions[i] = "D"+dirctions[i] 
            points[i] = (point[0],point[1]+max2)
    diss = [max2] + diss
    max2 >>= 1

if (bias == 0):
    diss = [1] + diss
    for i in range(m):
        dirctions[i] = "R"+dirctions[i]
print(len(diss))
for d in diss:
    print(str(d),end=" ")
print("")
for d in dirctions:
    print(d)

