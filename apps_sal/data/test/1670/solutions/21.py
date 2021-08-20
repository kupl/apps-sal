s1 = input()
s2 = input()
n = int(input())
a = []
for _ in range(n):
    (t, u, v, w) = input().split()
    a.append((int(t), u, int(v), w))
a.sort()
xs = set()
ys = set()
for (t, u, v, w) in a:
    if (u, v) in ys:
        continue
    if w == 'y':
        if (u, v) in xs:
            ys.add((u, v))
            print(s1 if u == 'h' else s2, v, t)
        else:
            xs.add((u, v))
    else:
        ys.add((u, v))
        print(s1 if u == 'h' else s2, v, t)
