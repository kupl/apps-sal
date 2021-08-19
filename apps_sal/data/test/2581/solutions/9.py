from sys import stdin
input = stdin.buffer.readline
n = int(input())
l = [[*map(int, input().split())] for _ in range(n)]
d = {}
su = {}
s = 0
an = [1, 1, 2, 1]
for i in range(n):
    for j in range(n):
        d[i - j] = d.get(i - j, 0) + l[i][j]
        su[i + j] = su.get(i + j, 0) + l[i][j]
position = [2, 1, 1, 1]
(x, y) = (0, 0)
for i in range(n):
    for j in range(n):
        p = d[i - j] + su[i + j] - l[i][j]
        if (i + j) % 2:
            if p > x:
                x = p
                position[:2] = [i + 1, j + 1]
        elif p > y:
            y = p
            position[2:] = [i + 1, j + 1]
print(x + y)
print(*position)
