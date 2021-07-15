n = int(input())
a = []
for i in range(n):
    s = input()
    a.append(s)
k = 0
for i in range(1, n - 1):
    for j in range(1, n - 1):
        if (a[i][j] == a[i - 1][j - 1] == a[i - 1][j + 1] == a[i + 1][j + 1] == a[i + 1][j - 1] == 'X'):
            k += 1
print(k)
