from sys import stdin, stdout
(n, m) = map(int, stdin.readline().split())
(p1, p2) = ([], [])
challengers = list(map(int, stdin.readline().split()))
for i in range(n):
    p1.append((challengers[i * 2], challengers[i * 2 + 1]))
challengers = list(map(int, stdin.readline().split()))
for i in range(m):
    p2.append((challengers[i * 2], challengers[i * 2 + 1]))
label = -1
X = 10
count = [0 for i in range(X)]
for x in range(1, X):
    for i in range(n):
        if x not in p1[i]:
            continue
        for j in range(m):
            if x not in p2[j]:
                continue
            if len(set(p1[i]) & set(p2[j])) == 1:
                count[x] += 1
                c = x
if count.count(0) == 9:
    stdout.write(str(c))
else:
    label = 1
    ind = 0
    for p11 in p1:
        cur = set()
        for p22 in p2:
            if len(set(p11) & set(p22)) == 1:
                cur |= set(p11) & set(p22)
        if len(cur) == 2:
            label = 0
    for p22 in p2:
        cur = set()
        for p11 in p1:
            if len(set(p11) & set(p22)) == 1:
                cur |= set(p11) & set(p22)
        if len(cur) == 2:
            label = 0
    if label == 1:
        stdout.write('0')
    else:
        stdout.write('-1')
