a, b, c, d = list(map(int, input().split()))
left = a + b
right = c + d

if left == right:
    print('Balanced')
elif left > right:
    print('Left')
else:
    print('Right')

