likes = int(input())
mas = input().split()
d = {}
for i in mas:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
maxx = max(d.values())
res = 0
for i in range(likes - 1, -1, -1):
    k = mas[i]
    if d[mas[i]] == maxx:
        res = mas[i]
        d[mas[i]] = 0
print(res)
