n, m, k = list(map(int, input('').split()))
x = {}
out = []
memory = []
for i in range(n):
    x[i] = list(map(int, input('').split()))
    out += [(0)]
for j in range(m):
    for i in range(n):
        k = x[i][j]
        if k != 0 and out[i] == 0:
            for q in range(n):
                if i != q:
                    for p in memory:
                        if p == k:
                            out[i] = j + 1
                            break
                    if k == x[q][j] and out[q] == 0:
                        out[i] = j + 1
                        out[q] = j + 1
                        memory += [(k)]

for i in range(n):
    print(out[i])
