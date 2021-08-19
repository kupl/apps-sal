def score(l):
    return sum((x * (x % 2 == 0) for x in l))


res = 0
ns = list(map(int, input().split()))
for i in range(14):
    l = list(ns)
    for j in range(13):
        l[(i + 1 + j) % 14] += l[i] // 14 + (1 if j + 1 <= l[i] % 14 else 0)
    l[i] = l[i] // 14
    res = max(res, score(l))
print(res)
