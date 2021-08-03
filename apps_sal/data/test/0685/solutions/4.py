import bisect

cl = list(map(int, input().split()))
n, h = cl[0], cl[1]
potok = []
pos = 0
smlist = []
sm = 0
pt = 0
mx = 0
smlist.append(0)
potok.append(0)
for i in range(n):
    s = input().split()
    pt += int(s[1]) - int(s[0])
    potok.append(pt)
    if i != 0:
        sm += int(s[0]) - pos
        smlist.append(sm)
    pos = int(s[1])

for i in range(n):
    pos = bisect.bisect_left(smlist, smlist[i] + h)
    res = potok[pos] - potok[i] + h
    if res > mx:
        mx = res


print(mx)
