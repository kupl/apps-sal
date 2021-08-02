n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))
a = []
b = []
for i in range(n):
    a.append([])
    b.append([])
    for j in range(n):
        a[i].append((arr[i][j] + arr[j][i]) / 2)
        b[i].append(arr[i][j] - a[i][j])
for i in range(n):
    print(*a[i])
for i in range(n):
    print(*b[i])
