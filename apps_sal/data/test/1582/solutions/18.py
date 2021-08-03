n = int(input())
d = [[0] * 10 for _ in range(10)]
for i in range(1, n + 1):
    d[int(str(i)[0])][i % 10] += 1
ret = 0
for s in range(10):
    for e in range(10):
        ret += d[s][e] * d[e][s]
print(ret)
