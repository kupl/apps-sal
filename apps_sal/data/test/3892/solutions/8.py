

import copy
r = input().split()
n = int(r[0])
m = int(r[1])
ar = [[] for i in range(n)]
for i in range(m):
    r = input().split()
    a = int(r[0])
    b = int(r[1])
    ar[a - 1].append(b - 1)
train = []
result = []
for i in range(n):
    count = m
    arr = copy.deepcopy(ar)
    time = copy.deepcopy(ar)
    ind = i
    res = 0
    for j in range(n):
        for k in range(len(arr[j])):
            if arr[j][k] >= j:
                time[j][k] = arr[j][k] - j
            else:
                time[j][k] = n - 1 - j + arr[j][k] + 1
    while (count != 0) or (len(train) != 0):
        if len(arr[ind]) != 0:
            train.append(arr[ind][time[ind].index(max(time[ind]))])
            del arr[ind][time[ind].index(max(time[ind]))]
            del time[ind][time[ind].index(max(time[ind]))]
            count -= 1
        while train.count(ind) != 0:
            train.remove(ind)
        ind += 1
        if ind == len(arr):
            ind = 0
        res += 1
    result.append(res - 1)
print(' '.join(map(str, result)))
