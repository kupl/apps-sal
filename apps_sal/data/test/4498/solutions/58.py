(a, b, c, d) = map(int, input().split())
x = abs(a - b)
y = abs(b - c)
z = abs(a - c)
if x <= d and y <= d:
    print('Yes')
elif z <= d:
    print('Yes')
else:
    print('No')
