from collections import Counter
(n, m) = map(int, input().split())
a = list(map(int, input().split()))
bc = [map(int, input().split()) for i in range(m)]
d1 = Counter(a)
d2 = {}
ans = 0
for (i, j) in bc:
    if j in d2:
        ref = d2[j]
        d2[j] = ref + i
    else:
        d2[j] = i
d = Counter(d1) + Counter(d2)
key = sorted(d)[::-1]
for i in key:
    qty = d[i]
    if qty < n:
        ans += qty * i
        n -= qty
    else:
        ans += n * i
        break
print(ans)
