def read():
    return map(int, input().split())


(n, m) = read()
a = [input() for i in range(n)]
y1 = x1 = 1000000000.0
y2 = x2 = -1
for i in range(n):
    if 'B' in a[i]:
        y1 = min(y1, i)
        y2 = max(y2, i)
        x1 = a[i].find('B')
        x2 = a[i].rfind('B')
x = (x1 + x2) // 2 + 1
y = (y1 + y2) // 2 + 1
print(y, x)
