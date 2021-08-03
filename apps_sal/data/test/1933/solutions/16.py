n, m, k = list(map(int, input().split()))
a = []
b = []
score = []
ct = 0

for i in range(n):
    a.append([int(x) for x in input().split()])


for i in range(m):
    b.append([])
for i in range(m):
    for j in range(n):
        b[i].append(a[j][i])

for i in range(m):
    maxsums = []
    for j in range(n):
        if b[i][j] == 1:
            if j + k < n:
                maxsums.append(sum(b[i][j:j + k]))
            else:
                maxsums.append(sum(b[i][j:]))
    try:
        score.append(max(maxsums))
        ct += maxsums.index(max(maxsums))
    except:
        pass
print(sum(score), ct)
