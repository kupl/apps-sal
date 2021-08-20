(ax, ay, bx, by, tx, ty) = list(map(int, input().split()))
od = []
co = []
objects = int(input())
for i in range(objects):
    (x, y) = list(map(int, input().split()))
    od.append(((tx - x) ** 2 + (ty - y) ** 2) ** 0.5)
    co.append([x, y])
asaved = [0, 0]
asaved2 = [0, 0]
ma = -10 ** 25
for i in range(objects):
    x = co[i][0]
    y = co[i][1]
    saved = od[i] - ((ax - x) ** 2 + (ay - y) ** 2) ** 0.5
    ma = max(ma, saved)
    if saved > asaved[0]:
        asaved2[0] = asaved[0]
        asaved2[1] = asaved[1]
        asaved[0] = saved
        asaved[1] = i
    elif saved > asaved2[0]:
        asaved2[0] = saved
        asaved2[1] = i
bsaved = [0, 0]
bsaved2 = [0, 0]
mb = -10 ** 25
for i in range(objects):
    x = co[i][0]
    y = co[i][1]
    saved = od[i] - ((bx - x) ** 2 + (by - y) ** 2) ** 0.5
    mb = max(mb, saved)
    if saved > bsaved[0]:
        bsaved2[1] = bsaved[1]
        bsaved2[0] = bsaved[0]
        bsaved[0] = saved
        bsaved[1] = i
    elif saved > bsaved2[0]:
        bsaved2[0] = saved
        bsaved2[1] = i
tot = 2 * sum(od)
if mb < 0 and ma < 0:
    tot -= max(mb, ma)
elif bsaved[1] == asaved[1]:
    tot -= max(asaved[0] + bsaved2[0], asaved2[0] + bsaved[0])
else:
    tot -= asaved[0] + bsaved[0]
print(tot)
