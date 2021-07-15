n = int(input())
a = [int(i) for i in input().split()]
p = []
for i in range(n):
    for j in range(i + 1, n):
        if a[i] == a[j] * 2:
            p.append([a[i], a[j]])
        if a[j] == a[i] * 2:
            p.append([a[j], a[i]])
        if a[i] == a[j] * 3:
            p.append([a[j], a[i]])
        if a[j] == a[i] * 3:
            p.append([a[i], a[j]])
d = dict()
d[p[0][0]] = 0
for j in range(n - 1):
    for i in range(n - 1):
        if d.get(p[i][0]) != None:
            d[p[i][1]] = d[p[i][0]] - 1
        if d.get(p[i][1]) != None:
            d[p[i][0]] = d[p[i][1]] + 1
ans = []
ans_p = []
for i, j in d.items():
    ans.append(i)
    ans_p.append(j)
prov = []
for i in range(len(ans_p)):
    prov.append(ans_p[i])
prov.sort()

while ans_p != prov:
    for i in range(n - 1):
        if ans_p[i] > ans_p[i + 1]:
            ans_p[i], ans_p[i + 1] = ans_p[i + 1], ans_p[i]
            ans[i], ans[i + 1] = ans[i + 1], ans[i]
for i in range(len(ans)):
    print(ans[i], end=' ')
