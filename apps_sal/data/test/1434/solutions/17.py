n = int(input())
verts = []
e = []
for i in range(n):
    inp = [*map(int, input().split(' '))]
    verts.append([i] + inp)

leavesQ = list(filter(lambda v: v[1] == 1, verts))

while len(leavesQ) > 0:
    l = leavesQ.pop()
    if l[1] != 1:
        continue
    l2 = verts[l[2]]
    e.append([l[0], l2[0]])

    l[1] -= 1
    l2[1] -= 1
    l2[2] ^= l[0]
    if l2[1] == 1:
        leavesQ.append(l2)

print(len(e))
for [x, y] in e:
    print(x, y)
