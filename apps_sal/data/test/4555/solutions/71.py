a, b, k = [int(x) for x in input().split()]
res = []
for i in range(a, min(b, k + a - 1) + 1):
    res.append(i)
for i in range(max(b - k + 1, a), b + 1):
    res.append(i)
res = list(set(res))
res.sort()
for i in range(len(res)):
    print(res[i])
