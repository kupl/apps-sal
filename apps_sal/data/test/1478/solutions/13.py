t = input().split(',')
k, m = 0, len(t)
p, d = [m] * m, [[] for i in range(m)]
for j in range(0, m, 2):
    while p[k] < 1:
        k -= 1
    p[k] -= 1
    d[k].append(t[j])
    k += 1
    p[k] = int(t[j + 1])
while d[k]:
    k += 1
print(k)
for q in d[:k]:
    print(*q)
