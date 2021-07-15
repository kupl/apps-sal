n = int(input())
a1 = list(map(int, list(input())))
u = list(map(int, input().split()))
a2 = []
for i in range(n):
    a2.append(u[a1[i] - 1])
ok = False
i1 = -1
for i in range(n):
    if a2[i] > a1[i]:
        i1 = i
        ok = True
        break
if ok:
    i2 = n
    for i in range(i1 + 1, n):
        if a2[i] < a1[i]:
            i2 = i
            break
    for i in range(i1, i2):
        a1[i] = a2[i]
print(''.join(map(str, a1)))

