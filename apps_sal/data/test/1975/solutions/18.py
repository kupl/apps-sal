a = list(map(int, input().split()))
b = [False for i in range(0, 101)]
f = [False for i in range(0, 101)]
sol = []
for i in range(1, a[0] + 1):
    for j in range(1, a[1] + 1):
        if not b[i] or not f[j]:
            b[i] = True
            f[j] = True
            sol.append((i, j))
print(len(sol))
for x in sol:
    print('%i %i' % x)
