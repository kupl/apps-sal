K = int(input())
res = [(0, 0)]
mm = 0
cands = []
for i in range(1, 1000):
    v = i
    for j in range(16):
        cands.append(v)
        v = 10 * v + 9
cands = list(sorted(set(cands)))
for x in cands:
    i = sum((ord(c) - ord('0') for c in str(x)))
    while x / i < res[-1][0]:
        res = res[:-1]
    res.append((x / i, x))
for i in range(1, K + 1):
    print(res[i][1])
