def I():
    return list(map(int, input().split()))


(n, m) = I()
a = [[]] * 10
indexwaliarray = [[0 for i in range(n)] for _ in range(m)]
for i in range(m):
    a[i] = list(I())
for i in range(m):
    for j in range(n):
        indexwaliarray[i][a[i][j] - 1] = j
answaliarray = [[a[0][i] - 1, a[0][i + 1] - 1] for i in range(n - 1)]
for i in range(n - 1):
    for j in range(1, m):
        if indexwaliarray[j][answaliarray[i][1]] != indexwaliarray[j][answaliarray[i][0]] + 1:
            answaliarray[i] = [-1, -1]
count = []
c = 0
for i in range(n - 1):
    if answaliarray[i] == [-1, -1]:
        if c != 0:
            count.append(c)
            c = 0
    else:
        c += 1
if c != 0:
    count.append(c)
yepakkaanshai = 0
for i in count:
    yepakkaanshai += (i + 1) * i // 2
print(yepakkaanshai + n)
