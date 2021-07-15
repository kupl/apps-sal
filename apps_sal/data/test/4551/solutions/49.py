a, b, c, d = map(int, input().split())
z = a + b - c - d
if z > 0:
    print('Left')
elif z < 0:
    print('Right')
else:
    print('Balanced')
