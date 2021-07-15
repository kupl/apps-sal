a = {}
b = {}
for i in range(int(input())):
    ID, val = [int(j) for j in input().split(' ')]
    a[ID] = val
for i in range(int(input())):
    ID, val = [int(j) for j in input().split(' ')]
    b[ID] = val

badA = []
badB = []
for k in a:
    if k in b and b[k] > a[k]:
        badA.append(k)
    elif k in b:
        badB.append(k)

for k in badA:
    del a[k]
for k in badB:
    del b[k]

s = 0
for k in a:
    s += a[k]
for k in b:
    s += b[k]
print(s)
