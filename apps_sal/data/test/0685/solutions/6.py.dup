n, h = map(int, input().split())
arr = []
for i in range(n):
    x, y = map(int, input().split())
    arr.append((x, y))
arr.sort()
arr1 = []
for i in range(n - 1):
    if(arr[i + 1][0] >= arr[i][1]):
        arr1.append(arr[i + 1][0] - arr[i][1])
    else:
        arr1.append(0)
fans = 0
sumx = 0
i = 0
j = 0
tempans = 0
while(i < n and j < n):
    while(j < n - 1 and sumx + arr1[j] < h):
        tempans += arr[j + 1][0] - arr[j][0]
        sumx += arr1[j]
        j += 1
    if(j == n - 1):
        tempans += h - sumx + arr[j][1] - arr[j][0]
        j += 1
        fans = max(tempans, fans)
    else:
        fans = max(tempans + arr[j][1] - arr[j][0] + h - sumx, fans)
        sumx -= arr1[i]
        tempans -= arr[i + 1][0] - arr[i][0]
        i += 1
print(fans)
