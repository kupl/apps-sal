r,c = list(map (int, input().split()))

horiz,vert = [], []

for i in range(r):
    horiz.append ([])
for i in range(c):
    vert.append ([])

for i in range (r):
    s = input()
    for j in range (c):
        horiz[i].append (s[j])
        vert[j].append (s[j])

ans = r * c
for i in range (r):
    for j in range (c):
        if ('S' in horiz[i]) and ('S' in vert[j]):
            ans -= 1
print (ans)

