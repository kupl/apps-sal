from collections import defaultdict
n, a, d = map(int, input().split())
if d == 0:
    print(1 if a == 0 else n + 1)
    return
if d < 0:
    a, d = -a, -d
dic = defaultdict(list)
for i in range(n + 1):
    l = a * i + (i - 1) * i // 2 * d
    r = a * i + (n - i + n - 1) * i // 2 * d
    dic[l % d].append((l, r))
res = 0
for p in dic.values():
    p.sort()
    r = -1000000000000000000
    for t in p:
        s, e = t
        if r < s:
            res += (e - s) // d + 1
            r = e
        if r < e:
            res += (e - r) // d
            r = e
print(res)
