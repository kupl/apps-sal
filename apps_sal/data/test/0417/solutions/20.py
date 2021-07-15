from collections import defaultdict
import sys
n, a, d = list(map(int, input().split(' ')))

if d == 0:
    print(1 if a == 0 else n + 1)
    return

if d < 0:
    a, d = -a, -d

dic = defaultdict(list)
for i in range(n + 1):
    l = a * i + i * (i - 1) // 2 * d
    r = a * i + (n-i + n-1)*i // 2 * d
    dic[l % d].append((l // d, r // d + 1))

ans = 0
for p in dic.values():
    end = -1e18
    p.sort()
    for t in p:
        s, e = t
        if end < s:
            ans += (e-s)
            end = e
        if end < e:
            ans += (e - end)
            end = e

print(ans)
