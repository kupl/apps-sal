w, h, n = map(int, input().split())
p = [0]
q = [w]
r = [0]
s = [h]
for i in range(n):
    x, y, a = map(int, input().split())
    if a == 1:
        p.append(x)
    elif a == 2:
        q.append(x)
    elif a == 3:
        r.append(y)
    else:
        s.append(y)
if max(p) <= min(q) and max(r) <= min(s):
    print((min(q) - max(p)) * (min(s) - max(r)))
else:
    print(0)
