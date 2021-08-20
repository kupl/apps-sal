a = input().split()
x1 = int(a[0])
y1 = int(a[1])
x2 = int(a[2])
y2 = int(a[3])
rook = 0
bishop = 0
king = 0
if (y1 == y2) ^ (x1 == x2):
    rook = 1
elif y1 == y2 and x1 == x2:
    rook = 0
else:
    rook = 2
if x1 == x2 and y1 == y2 or abs(x1 - x2) % 2 != abs(y1 - y2) % 2:
    bishop = 0
elif abs(x1 - x2) == abs(y1 - y2):
    bishop = 1
else:
    bishop = 2
while x1 != x2 and y1 != y2:
    if x1 < x2:
        x1 += 1
    elif x1 > x2:
        x1 -= 1
    if y1 < y2:
        y1 += 1
    elif y1 > y2:
        y2 += 1
    king += 1
while x1 != x2:
    if x1 < x2:
        x1 += 1
    elif x1 > x2:
        x1 -= 1
    king += 1
while y1 != y2:
    if y1 < y2:
        y1 += 1
    elif y1 > y2:
        y2 += 1
    king += 1
print(rook, bishop, king)
