def inp():
    return list(map(int, input().split()))


(n, m) = inp()
lines = [set([i]) for i in range(n + 1)]
for i in range(m):
    (x, y) = inp()
    lines[x].add(y)
    lines[y].add(x)
f = [True] * (n + 1)
for i in range(n):
    if f[i]:
        f[i] = False
        for j in lines[i]:
            f[j] = False
            if lines[i] != lines[j]:
                print('NO')
                quit()
print('YES')
