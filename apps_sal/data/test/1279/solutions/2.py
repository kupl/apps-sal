(n, m) = map(int, input().split())
l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))
x1 = 0
x2 = 0
y1 = 0
y2 = 0
for item in l1:
    if item % 2 == 0:
        x1 += 1
    else:
        x2 += 1
for item in l2:
    if item % 2 == 0:
        y1 += 1
    else:
        y2 += 1
print(min(x2, y1) + min(x1, y2))
