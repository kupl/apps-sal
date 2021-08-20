n = int(input())
arr = [int(x) for x in input().split()]
heights = 0
for i in range(1, len(arr)):
    if arr[i - 1] > arr[i]:
        heights += arr[i - 1] - arr[i]
        arr[i] = arr[i - 1]
print(heights)
