a, b = list(map(int, input().split(':')))
c, d = list(map(int, input().split(':')))
x = a * 60 + b
y = c * 60 + d
z = (x + y) // 2
print('%02d:%02d' % (z // 60, z % 60))
