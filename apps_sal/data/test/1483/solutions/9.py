n = int(input())
arr = list(map(int, input().split()))
arr.insert(0, 0)
arrx = []
for i in range(1, n + 1):
    arr1 = [0] * (n + 1)
    arr1[i] = 1
    flag = 0
    k = i
    ans = -1
    while flag == 0:
        if arr1[arr[k]] == 1:
            ans = arr[k]
            flag = 1
            break
        else:
            arr1[arr[k]] = 1
            k = arr[k]
    arrx.append(ans)
print(*arrx)
