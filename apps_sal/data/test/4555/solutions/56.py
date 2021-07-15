a, b, k = list(map(int, input().split()))
res = set()
for i in range(a, a + k):
    res.add(min(b, i))

for i in range(b, b - k, -1):
    res.add(max(a, i))

res = sorted(list(res))
for i in range(len(res)):
    print((res[i]))

