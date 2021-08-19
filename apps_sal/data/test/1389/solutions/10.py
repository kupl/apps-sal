(n, m) = [int(i) for i in input().split()]
l = []
for i in range(n):
    l.append(input())
la = [0 for i in range(m)]
s = 0
for i in range(n - 1, -1, -1):
    for j in range(m - 1, -1, -1):
        if l[i][j] == 'W':
            if la[j] != 1:
                x = 1 - la[j]
                s += 1
                for k in range(j, -1, -1):
                    la[k] += x
        elif la[j] != -1:
            x = -1 - la[j]
            s += 1
            for k in range(j, -1, -1):
                la[k] += x
print(s)
