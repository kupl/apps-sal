n = int(input())
arr = list(map(int, input().split()))
ansarr = [0] * n
flag = 0
dict1 = {}
dict2 = {}
for i in range(n):
    try:
        dict1[arr[i]].append(i)
    except:
        KeyError
        dict1[arr[i]] = [i]
        dict2[arr[i]] = 0
tempcount = 0
for i in dict1.keys():
    count = 0
    while dict2[i] < len(dict1[i]):
        if dict2[i] + n - i > len(dict1[i]):
            flag = 1
            break
        else:
            tempcount += n - i
            dict2[i] += n - i
if tempcount != n:
    flag = 1
if flag == 1:
    print('Impossible')
else:
    count = 0
    val = 1
    for i in dict1.keys():
        for j in range(0, len(dict1[i]), n - i):
            for k in range(n - int(i)):
                ansarr[dict1[i][j + k]] = val
            val += 1
    print('Possible')
    print(*ansarr)
