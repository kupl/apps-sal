import math
mod = 998244353
n = int(input())
arr = list(map(int, input().split()))
dict1 = {}
dict2 = {}
for i in range(len(arr)):
    try:
        dict1[arr[i]] += 1
        dict1[arr[i]] -= 1
        try:
            dict2[arr[i]][1] = i + 1
        except:
            KeyError
            dict2[arr[i]] = [dict1[arr[i]]]
            dict2[arr[i]].append(i + 1)
    except:
        KeyError
        dict1[arr[i]] = i + 1
arrx = []
for i in list(dict2.keys()):
    arrx.append((dict2[i][0], dict2[i][1]))
arrx.sort()
# print(*arrx)
count = 0
indexes = 0
if(len(arrx) == 0):
    print(pow(2, n - 1, mod))
else:
    flag = 0
    minval = arrx[0][0]
    maxval = arrx[0][1]
    if(minval == 1):
        count = -1
        flag = 1
    indexes = maxval - minval + 1
    for i in range(1, len(arrx)):
        if(arrx[i][0] > maxval):
            count += 1
            minval = arrx[i][0]
            maxval = arrx[i][1]
            indexes += maxval - minval + 1
        else:
            indexes += max(0, arrx[i][1] - maxval)
            maxval = max(maxval, arrx[i][1])
    count += 1
    rem = n - indexes
    # print(rem,count)
    if(flag == 1):
        countx = count + rem
    else:
        countx = count + rem - 1
    print(pow(2, countx, mod))
