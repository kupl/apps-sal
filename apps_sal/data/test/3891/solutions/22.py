n, m = map(int, input().split())
a = []
for i in range(n):
    b = input()
    a.append(b)
cou = 0
x = 0
y = 0
for i in range(n):
    for j in range(m):
        if a[i][j] == 'B' and cou == 0:
            x = i + 1
            y = j + 1
            cou += 1
        elif a[i][j] == 'B':
            cou += 1
    if cou > 0:
        print(x + cou // 2, y + cou // 2)
        return
