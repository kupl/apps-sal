n, m = list(map(int, input().split()))
t = list(map(int, input().split()))
mid = t.index(m)

lefts = [0] * 600000
lefts[300000] = 1
gt = 0
lt = 0
for i in range(mid - 1, -1, -1):
    if t[i] < m:
        lt += 1
    else:
        gt += 1
    lefts[300000 + gt - lt] += 1


rights = [0] * 600000
rights[300000] = 1
gt = 0
lt = 0
for i in range(mid + 1, n):
    if t[i] < m:
        lt += 1
    else:
        gt += 1
    rights[300000 + gt - lt] += 1


res = 0
for i in range(0, 210000):
    res += lefts[300000 - i] * rights[300000 + i]
    res += lefts[300000 - i] * rights[300000 + i + 1]
    if i != 0:
        res += lefts[300000 + i] * rights[300000 - i]
        res += lefts[300000 + i] * rights[300000 - i + 1]

print(res)
