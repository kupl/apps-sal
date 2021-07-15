#15:35

n = int(input())
circ = []
l = []

for i in range(n):
    a1, a2 = map(int, input().split())
    a1 -= 1
    a2 -= 1

    l.append((a1, a2))

circ.append(l[0][0])
circ.append(l[0][1])

for i in range(0, n - 1):
    p = l[circ[i]]
    
    if circ[i + 1] not in p:
        circ[i], circ[i + 1] = circ[i + 1], circ[i]

    p = l[circ[i]]

    if circ[i + 1] == p[0]:
        circ.append(p[1])

    else:
        circ.append(p[0])

for i in range(n):
    print(circ[i] + 1, end = ' ')

