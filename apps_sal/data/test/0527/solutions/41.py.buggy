from bisect import bisect_left, bisect
s = list(input())
sn = len(s)
t = list(input())
tn = len(t)
kouho = []
for i in range(26):
    kar = []
    now = chr(ord('a') + i)
    for j in range(sn):
        if s[j] == now:
            kar.append(j)
    kouho.append(kar)

cou = 0
now = -1
for i in range(tn):
    u = ord(t[i]) - ord("a")
    if kouho[u]:
        tugi = bisect(kouho[u], now)
        if tugi == len(kouho[u]):
            cou += 1
            now = kouho[u][0]
        else:
            now = kouho[u][tugi]
    else:
        print(-1)
        return

print(cou * sn + now + 1)
