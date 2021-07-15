n = int(input()) % 6
x = int(input())
p = [0, 1, 2]
for i in range(1, n + 1):
    if i % 2 == 1:
        p[0], p[1] = p[1], p[0]
    else:
        p[1], p[2] = p[2], p[1]
print(p[x])
