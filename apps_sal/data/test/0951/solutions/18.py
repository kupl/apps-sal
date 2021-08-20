k = int(input())
d = [0] * 10
s = input().strip()
for v in s:
    d[int(v)] += 1
res = 0
for (i, v) in enumerate(d):
    k -= i * v
if k < 0:
    k = 0
for (i, v) in enumerate(d):
    if k > (9 - i) * v:
        k -= (9 - i) * v
        res += v
    else:
        res += (k - 1) // (9 - i) + 1
        break
print(res)
