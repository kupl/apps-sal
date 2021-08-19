n = int(input())
arr = list(sorted(set(map(int, input().split()))))
if len(arr) == 1:
    print(0)
elif len(arr) == 2:
    if arr[1] % 2 == arr[0] % 2:
        print((arr[1] - arr[0]) // 2)
    else:
        print(arr[1] - arr[0])
elif len(arr) == 3:
    if arr[2] - arr[1] == arr[1] - arr[0]:
        print(arr[2] - arr[1])
    else:
        print(-1)
else:
    print(-1)
