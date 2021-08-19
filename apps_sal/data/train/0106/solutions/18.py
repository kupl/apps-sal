q = int(input())
for i in range(q):
    n = int(input())
    arr = [0 for i in range(n)]
    for i in range(n):
        temp = list(map(int, input().split()))
        temp.append(i)
        arr[i] = temp
    arr = sorted(arr, key=lambda l: l[0])
    # print(arr)
    ans = [1 for i in range(n)]
    # if(arr[0][1]<arr[1][0]):
    # 	ans[0]=2
    # 	for i in range(n):
    # 		print(ans[i],end=' ')
    # 	print()
    # 	continue
    # if(arr[n-1][0]>arr[n-2][1]):
    # 	ans[n-1]=2
    # 	for i in range(n):
    # 		print(ans[i],end=' ')
    # 	print()
    # 	continue
    yoyo = -1
    maxa = arr[0][1]
    for i in range(1, n):
        if(arr[i][0] > maxa):
            yoyo = i
            break
        if(arr[i][1] > maxa):
            maxa = arr[i][1]
    if(yoyo == -1):
        print(-1)
        continue
    else:
        for i in range(yoyo, n):
            ans[arr[i][2]] = 2
    for i in range(n):
        print(ans[i], end=' ')
    print()
