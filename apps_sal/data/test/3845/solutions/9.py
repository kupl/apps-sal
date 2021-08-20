(a, b) = map(int, input().split())
d = [['#'] * 100 for i in range(100)]
a -= 1
b -= 1
for i in range(50, 100):
    for j in range(100):
        d[i][j] = '.'
for i in range(0, 50, 2):
    for j in range(0, 100, 2):
        if a == 0:
            break
        d[i][j] = '.'
        a -= 1
    if a == 0:
        break
for i in range(99, 49, -2):
    for j in range(0, 100, 2):
        if b == 0:
            break
        d[i][j] = '#'
        b -= 1
print(100, 100)
for i in d:
    print(*i, sep='')
