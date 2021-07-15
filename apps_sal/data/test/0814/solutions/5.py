n = int(input())
a = [int(i) for i in input().split()]
d = [0] * max(a)
for i in a:
    for j in range(i):
        d[j] += 1
res = [0] * max(d)
for i in d:
    for j in range(i):
        res[j] += 1
res.reverse()
print(" ".join([str(i) for i in res]))
