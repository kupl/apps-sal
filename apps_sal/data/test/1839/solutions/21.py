n = int(input())
hor = set()
ver = set()
res = []
for i in range(n * n):
    h, v = map(int, input().split())
    if (h not in hor) and (v not in ver):
        res.append(str(i + 1))
        hor.add(h)
        ver.add(v)
print(" ".join(res))
