def chop():
    return (int(i) for i in input().split())


f = False
l, r, x, y, k = chop()
for i in range(x, y + 1):
    if i * k in range(l, r + 1):
        f = True
        break
print('YES' if f else 'NO')
