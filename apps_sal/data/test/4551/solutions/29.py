(a, b, c, d) = [int(x) for x in input().split()]
if a + b == c + d:
    print('Balanced')
elif a + b > c + d:
    print('Left')
else:
    print('Right')
