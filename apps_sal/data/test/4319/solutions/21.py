n = int(input())
a = [int(el) for el in input().split()]
col = 0
for i in range(n):
    if a[i] == 1:
        col += 1
print(col)
col = 1
for i in range(1, n):
    if a[i] == 1:
        print(a[i - 1], end=' ')
print(a[n - 1])
