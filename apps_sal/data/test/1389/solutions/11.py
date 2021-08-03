n, m = [int(i) for i in input().split()]
l = []
for i in range(n):
    l.append(input())
la = [0 for i in range(m)]
s = 0
for i in range(n - 1, -1, -1):
    cv = 0
    for j in range(m - 1, -1, -1):
        la[j] += cv
        if l[i][j] == 'W':
            if la[j] != 1:
                cv += 1 - la[j]
                la[j] = 1
                s += 1
        else:
            if la[j] != -1:
                cv += -1 - la[j]
                la[j] = -1
                s += 1
print(s)
