n, r = list(map(int, input().split()))
arr1 = []
arr2 = []
for i in range(n):
    x, y = list(map(int, input().split()))
    if(y >= 0):
        arr1.append((x, y))
    else:
        arr2.append((x, y))

arr1.sort()
arr2.sort(reverse=True)
currval = r
flag = 0
for i in range(len(arr1)):
    # print(arr1[i][0],currval)
    if(arr1[i][0] > currval):
        print("NO")
        return
    else:
        currval += arr1[i][1]
tempval = currval

mark = [0] * len(arr2)
countx = 0
finalans = 0
while(countx < len(arr2)):
    flag = -1
    for i in range(len(arr2)):
        if(mark[i] == 0 and currval >= arr2[i][0]):
            tempflag = 0
            for j in range(len(arr2)):
                if(j != i and mark[j] == 0):
                    if(currval + arr2[i][1] < arr2[j][0]):
                        tempflag = 1
                        break
            # print(tempflag)
            if(tempflag == 0):
                flag = i
                break
    if(flag == -1):
        finalans = 1
        break
    else:
        currval += arr2[flag][1]
        mark[flag] = 1
        countx += 1
if(currval < 0):
    finalans = 1
if(finalans == 0):
    print("YES")
else:
    mark = [0] * len(arr2)
    countx = 0
    finalans = 0
    currval = tempval
    while(countx < len(arr2)):
        flag = -1
        for i in range(len(arr2)):
            if(mark[i] == 0 and currval >= arr2[i][0]):
                tempflag = 0
                for j in range(len(arr2)):
                    if(j != i and mark[j] == 0):
                        if(currval + arr2[i][1] < arr2[j][0]):
                            tempflag = 1
                            break
                # print(tempflag)
                if(tempflag == 0):
                    flag = i

        if(flag == -1):
            print("NO")
            return
            break
        else:
            currval += arr2[flag][1]
            mark[flag] = 1
            countx += 1
    if(currval < 0):
        print("NO")
    else:
        print("YES")
