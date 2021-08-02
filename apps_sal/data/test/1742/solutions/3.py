n, m = list(map(int, input().split()))
p = list(map(int, input().split()))

allp = set()
for i in range(m):
    u, v = list(map(int, input().split()))
    allp.add((u, v))

currentList = [p.pop()]
suma = 0

while len(p) > 0:
    nextc = p.pop()
    check = True
    for i in currentList:
        if not ((nextc, i) in allp):
            check = False
            break

    if check:
        suma += 1
    else:
        currentList.append(nextc)

print(suma)
