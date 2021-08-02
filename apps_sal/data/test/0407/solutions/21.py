d = {}
f = {}
p = {}
n = int(input())
for i in range(n):
    l = input()
    f[l[0]] = 1
    t = 0
    for x in range(len(l) - 1, -1, -1):
        if l[x] in d:
            d[l[x]] += 10**t
        else:
            d[l[x]] = 10**t
        t += 1
y = list(d.items())
l = y[:]
y.sort(reverse=True, key=lambda x: x[1])
for (a, b) in y:
    if a not in f:
        p[a] = '0'
        y.remove((a, b))
        break
t = '123456789'
q = 0
for (a, b) in y:
    p[a] = t[q]
    q += 1


def f(m):
    return p[m]


qa = []
for (a, b) in l:
    w = int(f(a)) * b
    qa.append(w)
print(sum(qa))
