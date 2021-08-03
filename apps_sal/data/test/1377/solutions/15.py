n = int(input())
arr = list(map(int, input().split()))
maxa = max(arr)
maxi = arr.index(maxa)
flag = 0
for i in range(maxi):
    if arr[i] >= arr[i + 1]:
        flag = 1
        break
if flag == 1:
    print("NO")
else:
    flag = 0
    for i in range(maxi + 1, n):
        if arr[i] >= arr[i - 1]:
            flag = 1
            break
    if flag == 1:
        print("NO")
    else:
        print("YES")
