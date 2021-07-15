n = int(input())
line = input().split()
a = []
for d in line:
    a.append(int(d))
a.sort()

m = int(input())
line = input().split()
b = []
for d in line:
    b.append(int(d))
b.sort()

arr = [[0, 0, 0]]
i = 0
j = 0
k = 1
while i < n and j < m:
    if a[i] <= b[j]:
        if k > 0 and arr[k - 1][0] == a[i]:
            arr[k - 1][1] += 1
        elif k > 0:
            arr.append([a[i], arr[k - 1][1] + 1, arr[k - 1][2]])
            k += 1
        else:
            arr.append([a[i], 1, 0])
            k += 1
        i += 1
    else:
        if k > 0 and arr[k - 1][0] == b[j]:
            arr[k - 1][2] += 1
        elif k > 0:
            arr.append([b[j], arr[k - 1][1], arr[k - 1][2] + 1])
            k += 1
        else:
            arr.append([b[j], 0, 1])
            k += 1
        j += 1

while i < n:
    if arr[k - 1][0] == a[i]:
        arr[k - 1][1] += 1
    else:
        arr.append([a[i], arr[k - 1][1] + 1, arr[k - 1][2]])
        k += 1
    i += 1

while j < m:
    if arr[k - 1][0] == b[j]:
        arr[k - 1][2] += 1
    else:
        arr.append([b[j], arr[k - 1][1], arr[k - 1][2] + 1])
        k += 1
    j += 1

arr.append([0, n, m])

ans = [3 * n, 3 * m]
for lst in arr:
    tans = [2 * lst[1] + 3 * (n - lst[1]), 2 * lst[2] + 3 * (m - lst[2])]
    if tans[0] - tans[1] > ans[0] - ans[1]:
        ans = list(tans)

ans = str(ans[0]) + ':' + str(ans[1])
print(ans)

