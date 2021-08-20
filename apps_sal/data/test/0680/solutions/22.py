(x1, y1) = map(int, input().split())
(x2, y2) = map(int, input().split())
(x3, y3) = map(int, input().split())
base1 = {(x1, y1)}
for i in range(min(x2, x1), max(x2, x1) + 1):
    base1.add((i, y1))
for i in range(min(x3, x1), max(x3, x1) + 1):
    base1.add((i, y1))
for i in range(min(y2, y1), max(y2, y1) + 1):
    base1.add((x2, i))
for i in range(min(y3, y1), max(y3, y1) + 1):
    base1.add((x3, i))
base2 = {(x2, y2)}
for i in range(min(x2, x1), max(x2, x1) + 1):
    base2.add((i, y2))
for i in range(min(x3, x2), max(x3, x2) + 1):
    base2.add((i, y2))
for i in range(min(y2, y1), max(y2, y1) + 1):
    base2.add((x1, i))
for i in range(min(y3, y2), max(y3, y2) + 1):
    base2.add((x3, i))
base3 = {(x2, y2)}
for i in range(min(x3, x1), max(x3, x1) + 1):
    base3.add((i, y3))
for i in range(min(x3, x2), max(x3, x2) + 1):
    base3.add((i, y3))
for i in range(min(y3, y1), max(y3, y1) + 1):
    base3.add((x1, i))
for i in range(min(y3, y2), max(y3, y2) + 1):
    base3.add((x2, i))
ans = {}
if len(base1) < len(base2):
    ans = base1
else:
    ans = base2
if len(ans) > len(base3):
    ans = base3
print(len(ans))
for i in ans:
    print(*i)
