n = int(input())
xi = list(map(int,input().split()))

maxi = max(xi)
mini = min(xi)
mid = mini + (maxi - mini) // 2

if 2 > maxi - mini:
    print(n)
    for i in xi:
        print(i,end=" ")
else:
    temp = 0
    temp2 = 0
    temp3 = 0
    for i in xi:
        if i == mini:
            temp += 1
        elif i == mid:
            temp2 += 1
        else:
            temp3 += 1
    temp4 = maxi
    temp5 = temp3-temp
    if temp > temp3:
        temp4 = mini
        temp5 = temp - temp3
        temp = temp3
    temp6 = temp2
    temp2 //= 2
    if temp > temp2:
        temp *= 2
        print(n - temp)
        for i in range(temp5):
            print(temp4,end=" ")
        for i in range(n-temp5):
            print(mid,end=" ")
            
    else:
        print(n - temp2 * 2)
        for i in range(temp6 % 2):
            print(mid,end=" ")
        for i in range(temp2 + temp):
            print(mini,maxi,end=" ")
        for i in range(temp5):
            print(temp4,end=" ")

