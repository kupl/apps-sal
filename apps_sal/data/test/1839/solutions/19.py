N = int(input())
paintH = set()
paintV = set()
d = 0
res = []
for i in range(N):
    for j in range(N):
        d += 1
        h, v = list(map(int, input().split()))
        if h not in paintH and v not in paintV:
            paintH.add(h)
            paintV.add(v)
            res.append(str(d))

print(" ".join(res))

