from itertools import combinations
s = input()
n = int(input())

le = len(s)
tmp = s[:5]

for i in range(le - 4):
    tmp = min(tmp, s[i:i + 5])

seed = tuple(combinations(list(range(min(6, le + 1))), 2))
res = set()
for i, j in seed:
    res.add(tmp[i:j])
ans = sorted(res)
print((ans[n - 1]))
