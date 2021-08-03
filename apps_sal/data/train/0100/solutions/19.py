t = int(input())
for i in range(t):
    r, g, b = map(int, input().split())
    arr = [r, g, b]
    arr.sort()
    diff = arr[2] - arr[1]
    arr[2] -= arr[0]
    if arr[2] < arr[1]:
        arr[2] = int((arr[1] + arr[2]) / 2)
        arr[1] = arr[2]
    print(arr[0] + min(arr[2], arr[1]))
