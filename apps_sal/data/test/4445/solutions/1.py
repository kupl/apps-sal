n = int(input())
arr = list(map(int, input().split()))
arr1 = []
arr2 = []
for i in range(n):
    if arr[i] % 2 == 0:
        arr1.append(arr[i])
    else:
        arr2.append(arr[i])
arr1.sort(reverse=True)
arr2.sort(reverse=True)
if len(arr1) == len(arr2):
    print(0)
elif len(arr1) > len(arr2):
    l = len(arr2)
    print(sum(arr1) - sum(arr1[:l + 1]))
else:
    l = len(arr1)
    print(sum(arr2) - sum(arr2[:l + 1]))
