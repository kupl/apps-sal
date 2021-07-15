n, m, k = map(int,input().split())
x = 1
y = 1
add = 1
for pNum in range(k-1):
    print(2, end = ' ')
    print(x, y, end = ' ')
    y += add
    if y == m+1:
        y = m
        add = -1
        x = x + 1
    if y == 0:
        y = 1
        add = 1
        x = x + 1
    print(x, y, end = ' ')
    y += add
    if y == m+1:
        y = m
        add = -1
        x = x + 1
    if y == 0:
        y = 1
        add = 1
        x = x + 1
    print()
print(n * m - 2 * (k-1), end = ' ')
while x < n+1:
    print(x, y, end = ' ')
    y += add
    if y == m+1:
        y = m
        add = -1
        x = x + 1
    if y == 0:
        y = 1
        add = 1
        x = x + 1
print()
