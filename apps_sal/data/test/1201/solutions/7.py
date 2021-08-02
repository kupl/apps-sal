import copy
n = int(input())
arr = []
m = 0
for er in range(n):
    temp = list(map(int, input().split(" ")))
    temp.append(er + 1)
    if(temp[0] < temp[1]):
        arr.append(temp)
        if(temp[1] > m):
            m = temp[1]
    else:
        n -= 1
arr.sort(key=lambda x: x[1])
# print(arr)
temp = []
for i in range(n):
    temp.append([0])
com = []
com.append(temp)
total = [0, 0]
for i in range(1, m + 1):
    temp = []
    for j in range(n + 1):
        if(j == 0):
            temp.append([0])
        else:
            p = arr[j - 1]
            if(p[0] > i or p[1] <= i):
                temp.append(temp[j - 1])
            else:
                te = i - p[0]
                ty = copy.deepcopy(com[te][j - 1])
                ty[0] += p[2]
                ty.append(j)
                if(total[0] < ty[0]):
                    total = ty
                if(temp[j - 1][0] < ty[0]):
                    temp.append(ty)
                else:
                    temp.append(temp[j - 1])
    #print(temp , " temp")
    com.append(temp)
# print(com)
print(total[0])
if(total[0] > 0):
    print(len(total) - 1)
    for i in range(1, len(total)):
        print(arr[total[i] - 1][3], end=" ")
else:
    print("0")
