(n, m, sx, sy) = map(int, input().split())
used = [[False] * m for i in range(n)]
print(sx, sy)
for j in range(1, sy):
    print(sx, j)
for j in range(sy + 1, m + 1):
    print(sx, j)
for i in range(n, 0, -1):
    if i != sx:
        print(i, m)
j = m - 1
k = 0
while j:
    k += 1
    if k % 2 == 1:
        for i in range(1, n + 1):
            if i != sx:
                print(i, j)
    else:
        for i in range(n, 0, -1):
            if i != sx:
                print(i, j)
    j -= 1
