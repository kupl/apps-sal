n = int(input())
arr = list(map(int, input().rstrip().split()))
arr.sort()

if arr[n // 2 - 1] == arr[n // 2]:
    print((0))
else:
    print((arr[n // 2] - arr[n // 2 - 1]))
