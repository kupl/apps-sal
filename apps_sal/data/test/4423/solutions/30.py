n = int(input())
a = [input().split() for i in range(n)]
for i in range(n):
    a[i][1] = int(a[i][1])
    a[i].append(i + 1)
a.sort()
for i in range(100):
    for j in range(1, n):
        if a[j][0] == a[j - 1][0] and a[j][1] > a[j - 1][1]:
            (a[j - 1], a[j]) = (a[j], a[j - 1])
for i in range(n):
    print(a[i][2])
