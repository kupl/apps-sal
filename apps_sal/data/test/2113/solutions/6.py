n = int(input())
tr = {}
for i in range(1, n + 1):
    tm = []
    tr[i] = tm
for i in range(n - 1):
    (x, y) = list(map(int, input().strip().split(' ')))
    tr[x].append(y)
    tr[y].append(x)
a = set({})
b = set({})
sv = 0
q = [1]
ans = 0
a.add(1)
while len(q) > 0:
    x = q.pop(0)
    if a.__contains__(x):
        sv = 0
    elif b.__contains__(x):
        sv = 1
    for i in tr[x]:
        if sv == 0:
            if b.__contains__(i) == False:
                b.add(i)
                q.append(i)
        elif sv == 1:
            if a.__contains__(i) == False:
                a.add(i)
                q.append(i)
for i in a:
    ans += len(b) - len(tr[i])
print(ans)
