n = int(input())
d = {}
m = 0
for i in range(n):
    s = input()
    d[s] = d.get(s, 0) + 1
    if m <= d[s]:
        m = d[s]
c = []
for i in d:
    if d[i] == m:
        c.append(i)
c.sort()
for x in c:
    print(x)
