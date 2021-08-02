n = int(input())
d, d1 = {}, {}
for i in range(n):
    a, b = map(int, input().split())
    d[a], d1[b] = b, a
r = [list(filter(lambda f:d1.get(f) == None, d.keys()))[0], d.get(0)]
for i in range(2, n):
    r.append(d.get(r[i - 2]))
print(*r)
