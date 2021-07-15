a, b, c, d = list(map(int, input().split()))
left = a+b
right = c+d
print((['Balanced', 'Left', 'Right'][left > right or -(right > left)]))


