n = int(input())
m = []
a = []
for i in range(n):

    m.append(list(map(int, input().split())))
comp = 0
for i in range(n):
    if i == 0:
        comp = max(m[i][0], m[i][1])
        a.append(comp)
        continue
    maxa = max(m[i][0], m[i][1])
    mina = min(m[i][0], m[i][1])
    if maxa <= comp:
        comp = maxa
        a.append(comp)
    else:
        comp = mina
        a.append(comp)
for i in range(0, len(a) - 1):
    if a[i] < a[i + 1]:
        print("NO")
        return
print("YES")
