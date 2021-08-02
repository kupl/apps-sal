d = {}
n = int(input())
for _ in range(n - 1):
    a, b = map(int, input().split())
    d[a] = d.get(a, 0) + 1
    d[b] = d.get(b, 0) + 1
zz = list(filter(lambda x: d[x] > 2, d))
z = len(zz)
y = list(filter(lambda x: d[x] == 1, d))
if z > 1:
    print("No")
elif z == 0:
    print("Yes")
    print(1)
    print(*y)
else:
    print("Yes")
    print(len(y))
    for v in y:
        print(zz[0], v)
