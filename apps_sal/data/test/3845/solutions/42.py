a, b = map(int, input().split())
L = [["
qa, ra = divmod(a - 1, 50)
for i in range(qa):
    L[i * 2] = ["
L[qa * 2] = ["
qb, rb = divmod(b - 1, 50)
for i in range(qb):
    L[51 + i * 2] = ["." if j % 2 else "
L[51 + qb * 2] = ["." if j % 2 else "
print(100, 100)
for l in L:
    print(*l, sep="")
