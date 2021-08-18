n = int(input())
a = [[int(i) for i in input().split()] for j in range(n)]
for i in range(n):
    for j in range(i + 1, n):
        if a[i][0] != a[j][0] and a[i][1] != a[j][1]:
            print(abs(a[i][0] - a[j][0]) * abs(a[i][1] - a[j][1]))
            return
print(-1)
