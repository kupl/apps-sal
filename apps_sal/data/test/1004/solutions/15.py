
n = int(input())

ln = [int(i) for i in input().split(" ")]

seen = {}
sm = 0

f = True

tk = 0

pts = []

for i in range(0, len(ln)):
    sm += ln[i]
    if ln[i] < 0 and -ln[i] not in seen:
        f = False
    if ln[i] in seen:
        seen[ln[i]] += 1
        f = False
        break
    else:
        seen[ln[i]] = 1
    tk += 1
    if sm == 0:
        seen = {}
        pts.append(tk)
        tk = 0
if sm != 0:
    f = False

if not f:
    print(-1)
else:
    print(len(pts))
    print(" ".join([str(i) for i in pts]))
