from collections import Counter

n, m = map(int, input().split())
a = Counter(list(map(int, input().split())))
bc = [map(int, input().split()) for i in range(m)]
b = {}
ans = 0

for i, j in bc:
    if j in b:
        ref = b[j]
        b[j] = ref + i
    else:
        b[j] = i

d = Counter(a) + Counter(b)
keys = sorted(d)[::-1]

for key in keys:
    qty = d[key]
    if qty < n:
        ans += qty * key
        n -= qty
    else:
        ans += n * key
        break

print(ans)
