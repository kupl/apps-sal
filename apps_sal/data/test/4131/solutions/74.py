n, m = map(int, input().split())
l = [[] for i in range(m)]
for i in range(m):
    a, b = map(int, input().split())
    l[i] = [a, b, i]
l = list(sorted(l, key=lambda x: (x[0], x[1])))
ans = [[] for i in range(m)]
x = 0
y = 1
for i in range(m):
    if x != l[i][0]:
        x = l[i][0]
        y = 1
    else:
        y += 1
    a = str(x).zfill(6)
    b = str(y).zfill(6)
    ans[i] = [a + b, l[i][2]]
ans = list(sorted(ans, key=lambda x: x[1]))
for i in range(m):
    print(ans[i][0])
