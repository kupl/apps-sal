n = int(input())
a = list(map(int,input().split()))

arr = []
for i in range(n):
    arr.append(a[i] - (i+1))

sorted_arr = sorted(arr)
if n % 2 == 1:
    val = sorted_arr[n//2]
    for i in range(n):
        arr[i] = arr[i] - val
    print(sum([abs(i) for i in arr]))
else:
    arr1 = []
    arr2 = []
    val1 = sorted_arr[n//2]
    val2 = sorted_arr[n//2 - 1]
    for i in range(n):
        arr1.append(arr[i] - val1)
        arr2.append(arr[i] - val2)
    print(min(sum([abs(i) for i in arr1]),sum([abs(i) for i in arr2])))
