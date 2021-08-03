n, m, k = [int(i) for i in input().split()]
l = []
for i in range(n):
    l.append([int(j) for j in input().split()])
changes = 0
score = 0
for j in range(m):
    max = 0
    c1 = 0
    for i in range(n):
        l1 = []
        if (i <= n - k):
            for z in range(k):
                l1.append(l[i + z][j])
        else:
            for z in range(i, n):
                l1.append(l[z][j])
        if (l1[0] == 1):
            c2 = l1.count(1)
            if (c2 > max):
                max = c2
        else:
            continue
    if (max == 0):
        if (n == 1):
            if (l[0][j] == 1):
                score += 1
    else:
        for i in range(n):
            l1 = []
            if (i <= n - k):
                for z in range(k):
                    l1.append(l[i + z][j])
            else:
                for z in range(i, n):
                    l1.append(l[z][j])
            if (l1[0] == 1):
                c2 = l1.count(1)
                if (c2 == max):
                    score += max
                    changes += c1
                    break
                else:
                    c1 += 1
print(score, changes)
