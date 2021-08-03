from itertools import accumulate
n, k, q = list(map(int, input().split()))
count = [0 for _ in range(200002)]

for _ in range(n):
    l, r = list(map(int, input().split()))
    count[l] += 1
    count[r + 1] -= 1

ok = 0
count2 = [0 for _ in range(200002)]
for i, v in enumerate(count):
    ok += v
    if ok >= k:
        count2[i] = 1
    else:
        count2[i] = 0
prefixe = list(accumulate(count2))
res = []
for _ in range(q):
    l, r = list(map(int, input().split()))
    res.append(str(prefixe[r] - prefixe[l - 1]))
print('\n'.join(res))
