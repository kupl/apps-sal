n = int(input())
arr = list(map(int, input().split()))
for i in range(n - 2, -1, -1):
    if arr[i] > arr[i + 1]:
        arr[i] -= 1
        if arr[i] > arr[i + 1]:
            print('No')
            break
else:
    print('Yes')
