n = int(input())
a = []
for i in range(n):
    t, d, p = list(map(int, input().split()))
    a.append([t, d, p, i + 1])
a.sort(key=lambda x: x[1])
d = {0: [0, []]}
for i in a:
    e = {}
    for j in d:
        if d[j][0] + i[0] < i[1]:
            if j + i[2] in d:
                if d[j][0] + i[0] < d[j + i[2]][0]:
                    e[j + i[2]] = [d[j][0] + i[0], d[j][1] + [i[3]]]
            else:
                e[j + i[2]] = [d[j][0] + i[0], d[j][1] + [i[3]]]
    d.update(e)
t = max(d)
print(t)
k = d[t][1]
print(len(k))
k = list(map(str, k))
print(' '.join(k))
