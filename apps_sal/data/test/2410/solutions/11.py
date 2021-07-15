def ans(arr, n):
    left = arr[0]
    if left <= 0:
        return False
    for i in range (1, n):
        left += arr[i]
        if left <= 0:
            return False
    right = arr[n - 1]
    if right <= 0:
        return False
    i = n - 2
    while i >= 0:
        right += arr[i]
        if right <= 0:
            return False
        i -= 1
    return True
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    if ans(arr, n):
        print("YES")
    else:
        print("NO")
