(a, b, c, d) = map(int, input().split(' '))
dy = (d - b) // 2 + 1
dx = c - a + 1
print(dy * dx - dx // 2)
