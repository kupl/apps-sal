x, y, m = map(int, input().split())
if x > y:
    x, y = y, x
if y >= m:
    print(0)
    return
if y <= 0:
    print(-1)
    return
anw = 0

if x < 0:
    anw += abs(x) // y
    x += (abs(x) // y) * y
#print("anw aft", anw, x)
while max(x, y) < m:
    if x > y:
        x, y = y, x
    x = y + x
    anw += 1
print(anw)
