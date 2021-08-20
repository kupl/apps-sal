(n, m) = list(map(int, input().split()))
arr1 = sorted(list(map(int, input().split())))
arr2 = sorted(list(map(int, input().split())))
for i in range(n):
    if arr1[i] in arr2:
        print(arr1[i])
        break
else:
    mn1 = min(arr1)
    mn2 = min(arr2)
    if mn1 < mn2:
        print(mn1 * 10 + mn2)
    else:
        print(mn2 * 10 + mn1)
