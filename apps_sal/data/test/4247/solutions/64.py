n = int(input())
p = list(map(int, input().split()))
c = 0
for i in range(n - 2):
    l = []
    l2 = []
    l.append(p[i])
    l.append(p[i + 1])
    l.append(p[i + 2])
    l2.append(p[i])
    l2.append(p[i + 1])
    l2.append(p[i + 2])
    l2.remove(max(l))
    l2.remove(min(l))
    if l2[0] == l[1]:
        c += 1
print(c)
