n, m, k = [int(i) for i in input().split()]
a = [[0, 0] for i in range(m+1)]
p = [int(i) for i in input().split()]
s = [int(i) for i in input().split()]
f = [int(i) for i in input().split()]
for i in range(n):
    num = i + 1
    sk = s[i]
    po = p[i]
    if(po > a[sk][1]):
        a[sk][0] = num
        a[sk][1] = po
l = set()
for i in range(1, m+1):
    l.add(a[i][0])
f = set(f)
f -= l
print(len(f))
