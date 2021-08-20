(h, w) = map(int, input().split())
r = range(10)
c = [[int(i) for i in input().split()] for _ in r]
a = [[int(i) for i in input().split()] for _ in range(h)]
for k in r:
    for i in r:
        for j in r:
            c[i][j] = min(c[i][j], c[i][k] + c[k][j])
else:
    print(sum((c[i][1] for i in sum(a, []) if i != -1)))
