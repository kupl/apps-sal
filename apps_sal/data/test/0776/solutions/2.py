(a, b, c) = map(int, input().split())
m = int(input())
usb = []
ps2 = []
for i in range(m):
    (aa, bb) = input().split()
    if bb == 'USB':
        usb.append(int(aa))
    else:
        ps2.append(int(aa))
usb.sort()
ps2.sort()
equip = 0
cost = 0
t = min(a, len(usb))
equip += t
for i in range(t):
    cost += usb[i]
p = min(b, len(ps2))
equip += p
for i in range(p):
    cost += ps2[i]
rest = usb[t:] + ps2[p:]
rest.sort()
k = min(c, len(rest))
equip += k
for i in range(k):
    cost += rest[i]
print(equip, cost)
