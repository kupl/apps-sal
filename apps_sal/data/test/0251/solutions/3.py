n, k = [int(i) for i in input().split()]
h = [int(i) for i in input().split()]
h.sort()
hh = h[0]
for i in range(len(h)):
    h[i] -= hh
g = [0] * h[-1]
last = 0
for i in range(1, len(h)):
    if h[i] > h[i - 1]:
        for j in range(last, h[i]):
            g[j] = n - i
            last = h[i]
g.reverse()
s = 0
ans = 0
for i in range(len(g)):
    if s + g[i] > k:
        ans += 1
        s = g[i]
    else:
        s += g[i]
if s > 0:
    ans += 1
print(ans)
