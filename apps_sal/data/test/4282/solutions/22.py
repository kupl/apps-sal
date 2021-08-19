n = int(input())
arr = [-1]
a = [[]]
for i in range(n):
    a.append(list(map(int, input().split())))
arr.append(1)
if a[1][0] not in a[a[1][1]]:
    arr.append(a[1][0])
    arr.append(a[1][1])
else:
    arr.append(a[1][1])
    arr.append(a[1][0])
while len(arr) < n + 1:
    if a[arr[-2]][0] != arr[-1]:
        arr.append(a[arr[-2]][0])
    else:
        arr.append(a[arr[-2]][1])
for i in range(1, len(arr) - 1):
    print(arr[i], end=' ')
print(arr[n])
