n = int(input())
mas = []
cou = []
for i in range(n + 1):
    mas.append([])
    cou.append(0)
for i in range(n - 2):
    a, b, c = list(map(int, input().split()))
    mas[a].append([a, b, c])
    mas[b].append([a, b, c])
    mas[c].append([a, b, c])
    cou[a] += 1
    cou[b] += 1
    cou[c] += 1
for i in range(1, n + 1):
    if cou[i] == 1:
        x = i
        break
y = -1
for i in range(1, n + 1):
    if cou[i] == 2:
        if y == -1:
            y = i
        else:
            z = i
if not(y in mas[x][0]):
    y = z
for i in mas[x][0]:
    if i != x and i != y:
        z = i
        break
ans = [x, y, z]
for k in range(3, n):
    x = ans[k - 3]
    y = ans[k - 2]
    z = ans[k - 1]
    for i in mas[y]:
        if y in i and z in i and not(x in i):
            for j in range(len(i)):
                if i[j] != y and i[j] != z:
                    h = i[j]
                    break
    ans.append(h)
print(*ans)
