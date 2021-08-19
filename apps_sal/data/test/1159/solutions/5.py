import sys
n = int(sys.stdin.readline().strip())
P = []
i = 2
v = True
while v == True:
    w = True
    for p in P:
        if i % p == 0:
            w = False
    if w == True:
        P.append(i)
        if i >= n:
            v = False
            e = i
    i = i + 1
E = [[1, n]]
for i in range(0, n - 1):
    E.append([i + 1, i + 2])
m = n
i = 0
while e > m:
    E.append([i + 1, i + 1 + n // 2])
    m = m + 1
    i = i + 1
print(len(E))
for i in range(0, len(E)):
    print(str(E[i][0]) + ' ' + str(E[i][1]))
