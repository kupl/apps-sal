n = int(input())
g = {}
s = set()
bol = True
for i in range(1, 2000):
    g[i] = []

for j in range(2, n + 1):
    a = int(input())
    s.add(a)
    g[a].append(j)

for k in s:
    d = 0
    for h in g[k]:
        if h not in s:
            d = d + 1

    if d < 3:
        bol = False
if bol:
    print("Yes")
else:
    print("No")
