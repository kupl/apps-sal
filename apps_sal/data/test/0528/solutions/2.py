n, m = [int(x) for x in input().split()]

l = []
for i in range(m):
    x, y = [int(x) for x in input().split()]
    if x > y:
        x, y = y, x
    l.append((x, y))
l.sort(key=lambda x: x[0])

labels = {}
rels_count = {}
class_count = {}
for x, y in l:
    if x not in labels:
        labels[x] = len(rels_count)
        rels_count[labels[x]] = 0
        class_count[labels[x]] = 1
    if y not in labels:
        class_count[labels[x]] += 1
    labels[y] = labels[x]
    rels_count[labels[x]] += 1

flag = True
for i in range(len(rels_count)):
    l_n = class_count[i]
    l_m = rels_count[i]
    if l_n * (l_n - 1) != 2 * l_m:
        flag = False
        break
if flag:
    print("YES")
else:
    print("NO")
