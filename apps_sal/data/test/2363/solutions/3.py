n = int(input())
y = []
for x in range(n):
    y.append(input())

for x in y:
    noop = 0
    lst1 = x.split()
    lst1 = [int(p) for p in lst1]
    ma = max(lst1)
    mi = min(lst1)

    while(ma != 0 and mi != 0):
        b = ma // mi
        ma = ma - b * mi
        temp = ma
        ma = mi
        mi = temp
        noop += b
    print(noop)
