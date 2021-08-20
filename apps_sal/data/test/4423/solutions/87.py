n = int(input())
L = []
for i in range(n):
    c = []
    (a, b) = map(str, input().split())
    c.append(a)
    c.append(100 - int(b))
    c.append(i + 1)
    L.append(c)
L.sort()
for j in range(n):
    print(L[j][2])
