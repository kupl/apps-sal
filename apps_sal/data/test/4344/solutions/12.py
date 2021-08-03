n, k = map(int, input().split())
arr = list(map(int, input().split()))
arr1 = []
arr2 = []
for i in range(n):
    if(arr[i] not in arr1):
        arr1.append(arr[i])
        arr2.append(i + 1)
if(len(arr1) < k):
    print("NO")
else:
    print("YES")
    print(*arr2[:k])
