(n, k) = list(map(int, input().split()))
arr = list(map(int, input().split()))
arr = sorted(arr)
if k == 0:
    if arr[0] - 1 >= 1:
        print(arr[0] - 1)
    else:
        print(-1)
elif k > n:
    print(-1)
elif k == n:
    print(arr[k - 1])
elif arr[k] == arr[k - 1]:
    print(-1)
else:
    print(arr[k - 1])
