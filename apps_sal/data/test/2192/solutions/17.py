
n = int(input())
l = []
l1 = []
l2 = []
for i in range(n):
    k = list(map(int, input().split()))
    l.append(k)
    l1.append([0] * len(k))
    l2.append([0] * len(k))

for i in range(n):
    for j in range(n):
        l1[i][j] = (l[i][j] + l[j][i]) / 2
        l2[i][j] = (l[i][j] - l[j][i]) / 2

for i in range(n):
    print(*l1[i])
for i in range(n):
    print(*l2[i])
