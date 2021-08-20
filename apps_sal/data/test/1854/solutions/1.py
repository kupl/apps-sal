n = int(input())
a = [0]
sum = 0
for i in map(int, input().split()):
    a.append(i)
    sum += i
last = 0
ans = 0
edge = []
for i in range(1, n + 1, 1):
    if a[i] == 1:
        last = i
a[last] = 0
for i in range(1, n + 1, 1):
    if a[i] > 1:
        if last:
            edge.append([last, i])
            ans += 1
        last = i
for i in range(1, n + 1, 1):
    if a[i] == 1 and last:
        edge.append([last, i])
        last = 0
        a[i] = 0
        ans += 1
for i in range(1, n + 1, 1):
    for j in range(1, n + 1, 1):
        if a[j] == 1 and a[i] > 2:
            edge.append([i, j])
            a[i] -= 1
            a[j] -= 1
if len(edge) != n - 1:
    print('NO')
else:
    print('YES', ans)
    print(len(edge))
    for i in edge:
        print(i[0], i[1])
