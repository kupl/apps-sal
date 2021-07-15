def find(v: int, s: int):
    nonlocal d, a, n
    left, r = 0, v
    if s == -5:
        print('v', v, d[s][v], d[s][:v])
    while r - left > 1:
        mid = (left + r) // 2
        if s == -5 and v == 6:
            print(d[s][v][0], d[s][mid][1])
        if d[s][v][0] > d[s][mid][1]:
            left = mid
        else:
            r = mid
    return left


n = int(input())
a = list(map(int, input().split()))
d = dict()
for i in range(n):
    s = 0
    for j in range(i, n):
        s += a[j]
        if s in d:
            d[s].append((i + 1, j + 1))
        else:
            d[s] = [(i + 1, j + 1)]
for i in list(d.keys()):
    d[i].sort(key=lambda x: x[1])

# print(d)
ar = []
for el in list(d.keys()):
    cur = []
    r = 0
    for i in d[el]:
        if i[0] > r:
            cur.append(i)
            r = i[1]
    if len(ar) < len(cur):
        ar = cur

print(len(ar))
for i in ar:
    print(*i)

