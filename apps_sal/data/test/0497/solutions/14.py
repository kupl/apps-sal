n = int(input())
arr = [int(x) for x in input().split()]
if arr[0] != arr[n - 1]:
    print(n - 1)
else:
    c = arr[0]
    left = None
    right = None
    for i in range(n):
        if arr[i] != c:
            if left is None:
                left = i
            right = i
    print(max(n - 1 - left, right))
