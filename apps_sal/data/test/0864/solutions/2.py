n, m = list(map(int, input().split()))
d = {}
s = list(map(int, input().split()))
for c in s:
    if c in d:
        d[c] += 1
    else:
        d[c] = 1

d = list(d.values())

for k in range(m, 0, -1):
    l = 0
    for v in d:
        l += v // k
        if l >= n:
            print(k)
            return
print(0)

