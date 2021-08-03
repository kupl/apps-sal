x, y, a, b = list(map(int, input().split(' ')))

c = []

for p in range(a, x + 1):
    for q in range(b, y + 1):
        if(q < p):
            c.append((p, q))

print(len(c))
if c != []:
    for p in c:
        print(p[0], p[1])
