w, h, n = map(int, input().split())
s = [[1 for i in range(w)] for j in range(h)]
b = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
alist = []
for i in range(n):
    x, y, a = map(int, input().split())
    alist.append(a)
    if a == 1:
        for j in range(h):
            for k in range(0, x):
                s[j][k] = 0
    if a == 2:
        for j in range(h):
            for k in range(x, w):
                s[j][k] = 0
    if a == 3:
        for k in range(w):
            for j in range(0, y):
                s[j][k] = 0
    if a == 4:
        for k in range(w):
            for j in range(y, h):
                s[j][k] = 0
ans = 0
for i in range(h):
    ans = ans + s[i].count(1)
print(ans)
