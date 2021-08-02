n = int(input())
dict1 = {}
for i in range(n - 1):
    x, y = list(map(int, input().split()))
    try:
        dict1[y].append(x)
    except:
        KeyError
        dict1[y] = [x]
    try:
        dict1[x].append(y)
    except:
        KeyError
        dict1[x] = [y]
arr = list(map(int, input().split()))
if(arr[0] != 1):
    print("No")
else:
    j = 0
    i = 1
    flag = 0
    while(i < n and j < n):
        if(arr[j] in dict1[arr[i]]):
            i += 1
        else:
            j += 1
    if(j == n):
        print('No')
    else:
        print('Yes')
