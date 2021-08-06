from collections import defaultdict

LIM = 10 ** 5 + 123

n, m = list(map(int, input().split()))
occ = [[] for i in range(LIM)]
add = [0 for i in range(LIM)]


a = list(map(int, input().split()))

base_ans = 0
for i in range(1, m):
    if a[i] != a[i - 1]:
        occ[a[i]].append(a[i - 1])
        occ[a[i - 1]].append(a[i])

    t = abs(a[i] - a[i - 1])
    base_ans += t
    add[a[i]] += t
    add[a[i - 1]] += t

ans = base_ans


for i in range(LIM):
    if len(occ[i]) == 0:
        continue

    occ[i].sort()
    k = len(occ[i])
    sum_before = 0
    sum_after = sum(occ[i])

    for idx, c in enumerate(occ[i], 1):
        sum_before += c
        sum_after -= c

        cur = idx * c - sum_before
        cur += sum_after - (k - idx) * c
        ans = min(ans, base_ans - add[i] + cur)


print(ans)
