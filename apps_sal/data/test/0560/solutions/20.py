(a, b) = map(int, input().split())
(s, p) = (0, [[0] * b for i in range(a)])
for i in range(a):
    t = input()
    if 'S' in t:
        for j in range(b):
            p[i][j] |= 1
            if t[j] == 'S':
                for k in range(a):
                    p[k][j] |= 2
for i in range(a):
    s += p[i].count(3)
print(a * b - s)
