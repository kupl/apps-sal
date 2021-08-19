(n, m) = list(map(int, input().split()))
l = []
for i in range(m):
    (a, b, c) = list(map(int, input().split()))
    if len(l) <= c - 1:
        for i in range(c - len(l)):
            l.append([])
    p = l[c - 1]
    m = []
    for i in range(len(p)):
        if a in p[i] or b in p[i]:
            m.append(i)
    new = [a, b]
    for i in range(len(m)):
        new = new + p[m[i]]
    for i in range(len(m)):
        p.pop(m[i] - i)
    p.append(new)
    l[c - 1] = p
q = int(input())
for i in range(q):
    counter = 0
    (u, v) = list(map(int, input().split()))
    for j in range(len(l)):
        yes = 0
        for k in range(len(l[j])):
            if yes == 0 and u in l[j][k] and (v in l[j][k]):
                yes = 1
                counter += 1
    print(counter)
