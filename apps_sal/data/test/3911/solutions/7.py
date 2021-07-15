n = int(input())

L = []
for i in range(n):
    L.append(1)
    while len(L) >= 2 and L[-1] == L[-2]:
        L.pop()
        L[-1] += 1
print(' '.join(str(i) for i in L))

