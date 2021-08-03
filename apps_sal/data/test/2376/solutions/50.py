from collections import defaultdict
n, W = list(map(int, input().split()))
dd = defaultdict(list)
for i in range(n):
    weight, value = list(map(int, input().split()))
    dd[weight].append(value)

for k in list(dd.keys()):
    dd[k].sort(reverse=True)

a = min(dd.keys())
b, c, d = a + 1, a + 2, a + 3
ans = 0
for w in range(len(dd[a]) + 1):
    for x in range(len(dd[b]) + 1):
        for y in range(len(dd[c]) + 1):
            for z in range(len(dd[d]) + 1):
                if W < a * w + b * x + c * y + d * z:
                    continue
                val = sum(dd[a][:w]) + sum(dd[b][:x]) + \
                    sum(dd[c][:y]) + sum(dd[d][:z])
                ans = max(ans, val)
print(ans)
