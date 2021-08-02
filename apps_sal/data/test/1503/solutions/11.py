n, m = list(map(int, input().split()))
arr = []
arr1 = []
for i in range(m):
    arrx = list(map(int, input().split()))
    arry = [0] * n
    for j in range(n):
        arry[arrx[j] - 1] = j + 1
    arr.append(arrx)
    arr1.append(arry)

ans = n
i = 0
j = 1
flag = 0
while(i < n - 1 and j < n):
    k1 = arr[0][i]
    k2 = arr[0][j]
    l = 0
    while(l < m):
        # print(arr[0][i+k]-1,arr[0][i+k+1]-1,'YO',flag,l)
        if(arr1[l][arr[0][j - 1] - 1] != arr1[l][arr[0][j] - 1] - 1):
            flag = 1
            break
        # print(flag)
        if(flag == 1):
            break
        l += 1
    if(flag == 1):
        ans += ((j - i) * (j - i + 1)) // 2
        ans -= j - i
        i = j
        j += 1
        flag = 0
    else:
        j += 1
    # print(i,j)
if(flag == 0):
    ans += ((j - i) * (j - i + 1)) // 2
    ans -= j - i
print(ans)
