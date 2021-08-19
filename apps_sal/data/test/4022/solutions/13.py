n = int(input())
(l, r) = ([], [])
(a, b) = (0, 0)
for i in range(n):
    (a, b) = list(map(int, input().split()))
    l.append(a)
    r.append(b)
minr = 10 ** 10
maxl = -1
l1 = -1
r1 = -1
for i in range(n):
    if l[i] > maxl:
        maxl = l[i]
        l1 = i
    if r[i] < minr:
        minr = r[i]
        r1 = i
l_1 = l.copy()
l_2 = l.copy()
r_1 = r.copy()
r_2 = r.copy()
l_1.pop(l1)
r_1.pop(l1)
l_2.pop(r1)
r_2.pop(r1)
print(max(0, min(r_1) - max(l_1), min(r_2) - max(l_2)))
