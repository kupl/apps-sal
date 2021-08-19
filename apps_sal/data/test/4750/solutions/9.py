t = int(input())
ansarr = []
for l in range(t):
    arr = list(map(int, input().split()))
    if arr[0] == arr[2]:
        ansarr.append(arr[0])
        ansarr.append(arr[0] + 1)
    else:
        ansarr.append(arr[0])
        ansarr.append(arr[2])
print(*ansarr)
