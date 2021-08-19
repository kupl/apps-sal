((n, m), *d) = [list(map(int, s.split())) for s in open(0)]
d.sort()
l = [0] * n
for i in range(m):
    d[i] = [d[i][0] - 1, d[i][1] - 1]
    l[d[i][0]] += 1
p = [0] * n
p[0] = 1
for x in d:
    p[x[1]] += p[x[0]] / l[x[0]]
e = [0] * n
index = d[-1][0]
max_in_index = 0
max_reduce_e = 0
for x in d[::-1] + [[-1, -1]]:
    if index != x[0]:
        if l[index] > 1:
            max_reduce_e = max(max_reduce_e, p[index] * (e[index] / l[index] - (e[index] - max_in_index) / (l[index] - 1)))
        e[index] /= l[index]
        index = x[0]
        max_in_index = 0
    max_in_index = max(max_in_index, e[x[1]] + 1)
    e[x[0]] += e[x[1]] + 1
print(e[0] - max_reduce_e)
