n = int(input())
arr = list(map(int, input().split()))
maxval = max(arr)
maxindex = -1
for i in range(n):
    if(arr[i] == maxval):
        maxindex = i
        break

flag = 0
temp = maxval
for i in range(maxindex - 1, -1, -1):
    if(temp <= arr[i]):
        flag = 1
        break
    else:
        temp = arr[i]

temp = maxval
for i in range(maxindex + 1, n):
    if(arr[i] >= temp):
        flag = 1
        break
    else:
        temp = arr[i]

if(flag == 0):
    print("YES")
else:
    print("NO")
