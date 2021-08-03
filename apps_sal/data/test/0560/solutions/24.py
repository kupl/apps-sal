r, c = list(map(int, input().split()))
a = []
for i in range(r):
    a.append(input())

x = r
for i in range(r):
    for j in range(c):
        if a[i][j] == 'S':
            x -= 1
            break

y = c
for j in range(c):
    for i in range(r):
        if a[i][j] == 'S':
            y -= 1
            break

print(x * c + r * y - x * y)
