arr = []
for i in input():
    arr.append(int(i))
ans1 = -1
n = len(arr)
for (i, x) in enumerate(arr):
    if x % 2 == 0:
        ans1 = i
if ans1 == -1:
    print(-1)
else:
    ans2 = -1
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] % 2 == 0 and arr[i] < arr[len(arr) - 1]:
            ans2 = i
    if ans2 == -1:
        (arr[n - 1], arr[ans1]) = (arr[ans1], arr[n - 1])
    else:
        (arr[n - 1], arr[ans2]) = (arr[ans2], arr[n - 1])
    for i in arr:
        print(i, end='')
