n = int(input())

ns = [0] * 10
nm = [0] * 10

s = list(map(int, input()))

for i in map(int, input()):
    nm[i] += 1

mi = ma = 0

cnm = nm[:]

for i in s:
    ok = False
    for j in range(i, 10):
        if cnm[j] != 0:
            cnm[j] -= 1
            ok = True
            break
    if not ok:
        mi += 1

cnm = nm[:]

for i in s:
    ok = False
    for j in range(i + 1, 10):
        if cnm[j] != 0:
            cnm[j] -= 1
            ok = True
            break
    if ok:
        ma += 1

print(mi)
print(ma)
