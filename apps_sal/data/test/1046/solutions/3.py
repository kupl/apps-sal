n, s = int(input()), 0
t = list(map(int, input().split()))
p = set(t)
p.discard(0)
for i in p:
    k = t.count(i)
    if k == 2: s += 1
    elif k > 2:
        s = -1
        break
print(s)
