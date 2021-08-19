(a, b, c, d) = map(int, input().split())
x = a + b
y = c + d
if x == y:
    print('Balanced')
elif x > y:
    print('Left')
else:
    print('Right')
