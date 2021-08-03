n, m = list(map(int, input().split()))
s = 0
v = [0 for i in range(m)]
for i in range(m):
    v[i] = [-1, 0]
for i in range(n):
    l = list(map(int, input().split()))
    c0 = -1
    c2 = 0
    for j in range(m):
        if l[j] == 1:
            if c0 == -1:
                c0 = j
            else:
                s -= 2

            if v[j][0] > -1:
                s -= 2
            else:
                v[j][0] = i
            v[j][1] = i
            c2 = j
    if c0 > -1:
        s += c0 + (c2 - c0) * 2 + m - c2 - 1

for i in range(m):
    if v[i][0] > -1:
        s += v[i][0] + (v[i][1] - v[i][0]) * 2 + n - v[i][1] - 1
print(s)
