[n, v] = input().split()
v1 = []
for i in range(3002):
    v1.append(0)
v = int(v)
maxx = 0
for i in range(int(n)):
    [a, b] = input().split()
    v1[int(a)] += int(b)
    maxx = max(int(a), maxx)
res = 0
for i in range(1, maxx + 2):
    delt = min(v, v1[i] + v1[i - 1])
    res += delt
    d = v1[i - 1] - delt
    v1[i] += min(d, 0)
print(res)
