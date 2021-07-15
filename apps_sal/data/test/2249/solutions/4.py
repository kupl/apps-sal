n = int(input())
l = [int(el) for el in input().split()]
col = 0
a = [0] * 100001
s = set()
for i in range(n):
    if a[l[i]] == 0:
        col += len(s)
        a[l[i]] += len(s)
        s.add(l[i])
    else:
        col += len(s) - a[l[i]]
        a[l[i]] = len(s)
        s.add(l[i])
print(col)

