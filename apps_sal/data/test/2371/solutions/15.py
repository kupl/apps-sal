n, z, w = map(int, input().split())
arr = list(map(int, input().split()))

if n == 1:
    print(abs(arr[0] - w))
else:
    print(max(abs(arr[-1] - w), abs(arr[-2] - arr[-1])))
