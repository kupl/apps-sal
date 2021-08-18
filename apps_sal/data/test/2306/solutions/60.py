N = int(input())
inl = list([int(x) * 2 for x in input().split()])
vs = list(map(int, input().split()))

sumtime = sum(inl)

limits = [0]
for i, t in enumerate(inl):
    for _ in range(t):
        limits.append(vs[i])

resv = [0]
for i in range(1, sumtime + 1):
    resv.append(min(resv[-1] + 0.5, limits[i]))

resv[sumtime] = 0
for i in reversed(list(range(1, sumtime + 1))):
    resv[i - 1] = min(resv[i] + 0.5, resv[i - 1], limits[i])

res = 0.0
for i in range(sumtime):
    res += (resv[i] + resv[i + 1]) * 0.5

print((res * 0.5))
