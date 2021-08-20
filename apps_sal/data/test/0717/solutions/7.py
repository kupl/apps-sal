from math import ceil
d = int(input())
a = list()
for k in range(d):
    (s, l) = input().split()
    a.append((int(s), int(l)))
t = a[0][0]
for i in a[1:]:
    (s, l) = i
    if s > t:
        t = s
    else:
        n = ceil((t - s + 1) / l)
        t = s + l * n
print(t)
