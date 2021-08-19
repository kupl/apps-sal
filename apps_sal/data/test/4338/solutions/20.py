(n, x, y) = map(int, input().split())
a = [int(j) for j in input().split()]
nLX = 0
for e in a:
    if e <= x:
        nLX += 1
if y >= x:
    print((nLX + 1) // 2)
else:
    print(n)
