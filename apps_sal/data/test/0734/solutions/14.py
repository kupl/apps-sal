n, m = map(int, input().split())
arr = [int(x) for x in input().split()]

arr = sorted(arr, reverse=True)
arr.append(0)
# print(arr)
isum = sum(arr)
ans = []
top = arr[0]
for i in range(n):
    if(arr[i] == 1):
        ans.append(1)
        arr[i + 1] = 1
        continue
    if(arr[i + 1] > arr[i]):
        arr[i + 1] = arr[i]
    if arr[i] - arr[i + 1] == 0:
        ans.append(1)
        h = 1
    else:
        ans.append(arr[i] - arr[i + 1])
        h = arr[i] - arr[i + 1]

    top = arr[i] - h
    arr[i + 1] = top
# 	print("top:",top)
# 	print("arr:",arr)
# 	print("ans:",ans)
# print(ans)
print(isum - sum(ans))
