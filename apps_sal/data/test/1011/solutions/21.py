read = lambda: map(int, input().split())
n = int(input())
a = sorted(read())[::-1]
m = int(input())
b = sorted(read())[::-1]
x, y = 2 * n, 2 * m
j = 0
for i in range(n):
    while j < m and b[j] >= a[i]:
        j += 1
    x1 = i + 1 + 2 * n
    y1 = j + 2 * m
    if x1 - y1 > x - y or (x1 - y1 == x - y and x1 > x):
        x, y = x1, y1
print(x, y, sep = ':')

