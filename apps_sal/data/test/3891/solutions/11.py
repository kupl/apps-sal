(n, m) = list(map(int, input().split()))

lst = []
for x in range(n):
    s = input()
    lst.append(s)

x1 = -1
y1 = -1

x2 = -1
y2 = -1

for x in range(n):
    for y in range(m):
        if lst[x][y] == "B" and x1 == -1:
            x1 = x
            y1 = y
        if lst[x][y] == "B":
            x2 = x
            y2 = y

print(x1 + (x2 - x1) // 2 + 1, y1 + (y2 - y1) // 2 + 1)

