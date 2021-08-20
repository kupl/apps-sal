(n, m) = map(int, input().split())
a = [0] * n
k = 0
for i in range(n):
    a[i] = list(map(int, input().split()))
for i in range(n):
    for j in range(0, 2 * m, 2):
        if a[i][j] == 1 or a[i][j + 1] == 1:
            k += 1
print(k)
