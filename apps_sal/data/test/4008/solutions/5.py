(n, k) = list(map(int, input().split()))
arr = list(map(int, input().split()))
dict1 = {}
for i in range(n):
    try:
        dict1[arr[i]].append(i)
    except:
        KeyError
        dict1[arr[i]] = [i]
flag = 0
colors = {}
for i in list(dict1.keys()):
    colors[i] = [0] * k
    if len(dict1[i]) > k:
        flag = 1
        break
if flag == 1:
    print('NO')
else:
    ansarr = [0] * n
    for i in range(k):
        ansarr[i] = i + 1
        colors[arr[i]][i] = 1
    val = 0
    for i in list(dict1.keys()):
        for j in dict1[i]:
            if ansarr[j] == 0:
                for l in range(k):
                    if colors[i][l] == 0:
                        ansarr[j] = l + 1
                        colors[i][l] = 1
                        break
    print('YES')
    print(*ansarr)
