n = int(input())
a = list()
x1, x2 = list(map(int, input().split()))
for i in range(n):
    k, b = list(map(int, input().split()))
    y1 = k * x1 + b
    y2 = k * x2 + b
    a.append((y1, y2))
a.sort()
fl = 'NO'
y1m = a[0][0]
y2m = a[0][1]
for y1, y2 in a:
    if y2 < y2m:
        fl = 'YES'
    else:
        y2m = max(y2m, y2)
print(fl)
