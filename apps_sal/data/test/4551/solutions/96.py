a, b, c, d = map(int, input().split())
left = a + b 
right = c + d

if left > right:
    print('Left')
elif left == right:
    print('Balanced')
else:
    print('Right')
