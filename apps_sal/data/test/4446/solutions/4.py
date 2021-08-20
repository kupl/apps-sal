from math import ceil
(n, a, b, k) = map(int, input().split())
h = list(map(int, input().split()))
for i in range(n):
    h[i] -= h[i] // (a + b) * (a + b)
    if h[i] == 0:
        h[i] += a + b
h.sort()
ans = 0
i = 0
while k > 0 and i < n:
    if ceil(h[i] / a) - 1 <= k:
        k -= ceil(h[i] / a) - 1
        ans += 1
    else:
        k = -1
    i += 1
print(ans)
