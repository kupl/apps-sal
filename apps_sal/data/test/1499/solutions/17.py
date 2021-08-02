s = input().split()
n, m = int(s[0]), int(s[1])

t = [0, 0, 0, 0]
x = []
k = 0
for i in range(n):
    x.append(t.copy())

for i in range(n):
    for j in (0, 3):
        if k == m:
            break
        k = k + 1
        x[i][j] = k
for i in range(n):
    for j in (1, 2):
        if k == m:
            break
        k = k + 1
        x[i][j] = k

s = ""
for i in range(n):
    for j in (1, 0, 2, 3):
        if x[i][j] != 0:
            s += str(x[i][j]) + ' '
print(s)
