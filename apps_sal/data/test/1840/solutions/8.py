(n, m) = list(map(int, input().split()))
d = list(map(int, input().split()))
l = []
for i in range(n):
    l.append([d[i], i])
l.sort()
l2 = []
for i in range(m):
    (a, b) = list(map(int, input().split()))
    l2.append([a, b])
l2.sort()
s = 0
j = 0
r = [0] * n
for i in range(n):
    while j < m and l2[j][0] <= l[i][0]:
        s += l2[j][1]
        j += 1
    r[l[i][1]] = s
print(' '.join(map(str, r)))
