n = int(input())
p = [0]
c = [0]
a = []
m = dict()
for i in range(n + 1):
    m[i] = []
for i in range(n):
    (x, y) = list(map(int, input().split()))
    p.append(x)
    c.append(y)
    if x != -1:
        m[x].append(i + 1)
for i in range(1, n + 1):
    if c[i] == 1:
        if len(m[i]) == 0:
            a.append(i)
        else:
            for j in m[i]:
                if c[j] == 0:
                    break
            else:
                a.append(i)
if len(a) == 0:
    print(-1)
else:
    print(*sorted(a))
