n = int(input())
ox = []
cx = []
l3 = []
oy = []
cy = []
for i in range(n):
    r, s, a, b = list(map(int, input().strip().split()))
    l3.append([r, s, a, b])
    ox.append(r)
    oy.append(s)
    cx.append(a)
    cy.append(b)
ox.sort()
cx.sort()
oy.sort()
cy.sort()
e1 = ox[-1]
e2 = cx[0]
e3 = oy[-1]
e4 = cy[0]

for i in l3:
    a1 = i[0]
    a2 = i[1]
    a3 = i[2]
    a4 = i[3]
    if a1 == e1:
        w = ox[-2]
    else:
        w = ox[-1]
    if a2 == e3:
        y = oy[-2]
    else:
        y = oy[-1]

    if a3 == e2:
        x = cx[1]
    else:
        x = cx[0]

    if a4 == e4:
        z = cy[1]
    else:
        z = cy[0]

    if(w <= x and y <= z):
        print(w, y)
        return
