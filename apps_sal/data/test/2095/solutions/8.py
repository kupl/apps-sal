n = int(input())
a = [list(map(int, input().split())) for i in range(n)]
a2 = [0] * n
for y in range(n):
    for x in range(n):
        if a[y][x] != -1:
            if a[y][x] == 1:
                a2[y] = 1
            elif a[y][x] == 2:
                a2[x] = 1
            elif a[y][x] == 3:
                a2[x] = 1
                a2[y] = 1
num = 0
for i in range(n):
    if a2[i] == 0:
        num += 1
print(num)
for i in range(n):
    if a2[i] == 0:
        print(i + 1, end=" ")
