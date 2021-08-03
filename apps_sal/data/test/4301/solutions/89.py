n = int(input())
xlist = [int(input()) for i in range(n)]
ylist = sorted(xlist)
max1 = ylist[-1]
max2 = ylist[-2]
for i in range(n):
    if xlist[i] != max1:
        print(max1)
    else:
        print(max2)
