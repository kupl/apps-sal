from collections import defaultdict
(H, W, M) = list(map(int, input().split()))
hw = [list(map(int, input().split())) for _ in range(M)]
d1 = defaultdict(int)
d2 = defaultdict(int)
b = defaultdict(int)
for (h, w) in hw:
    d1[h] += 1
    d2[w] += 1
    b[h, w] = 1
m1 = max(d1.values())
m2 = max(d2.values())
e1 = [k for k in d1.keys() if d1[k] == m1]
e2 = [k for k in d2.keys() if d2[k] == m2]
flag = True
for x in e1:
    for y in e2:
        if b[x, y] == 1:
            pass
        else:
            flag = False
            break
    if not flag:
        break
if flag:
    print(m1 + m2 - 1)
else:
    print(m1 + m2)
