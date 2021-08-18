N = int(input())
arr = list(map(int, input().split()))

arr = sorted(set(arr))
while True:
    # print(arr)
    minValue = arr[0]
    arr = [arr[i] % arr[0] for i in range(1, len(arr)) if arr[i] % arr[0] != 0]
    arr.append(minValue)
    arr = sorted(set(arr))
    if len(arr) == 1:
        print(arr[0])
        return
