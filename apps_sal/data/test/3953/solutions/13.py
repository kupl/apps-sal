n = int(input())
l = []
for _ in range(n):
    l.append([x for x in input()])

results = []
thing = True
for i in range(n):
    hit = False
    for j in range(n):
        if l[i][j] != "E":
            results.append(f"{i + 1} {j + 1}")
            hit = True
            break
    if not hit:
        thing = False
        break
if not thing:
    results = []
    thing = True
    for j in range(n):
        hit = False
        for i in range(n):
            if l[i][j] != "E":
                results.append(f"{i + 1} {j + 1}")
                hit = True
                break
        if not hit:
            thing = False
            break

if thing:
    for r in results:
        print(r)
else:
    print(-1)

