n, k = list(map(int, input().split()))
a = list(map(int, input().split()))
d = {}
for x in a:
    d[x] = d.get(x, 0) + 1
m = max(d.values())
if m % k == 0:
    sets = m // k
else:
    sets = m // k + 1
print(sets * len(d) * k - n)
