n = int(input())
a = list(map(int, input().split()))
(x, y, z) = (0, 0, 0)
for i in a:
    if i % 4 == 0:
        x += 1
    elif i % 2 == 0:
        y += 1
    else:
        z += 1
if x >= z - 1 + y % 2:
    print('Yes')
else:
    print('No')
