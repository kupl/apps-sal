n = int(input())
a = [int(x) for x in input().split()]
s = set()
d = dict()
c = [0] * n
for i in range(n - 1, -1, -1):
    c[i] = len(s)
    s.add(a[i])
    d[a[i]] = i
ans = 0
for k in list(d.keys()):
    pos = d[k]
    ans += c[pos]
print(ans)
