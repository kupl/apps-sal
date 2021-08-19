(n, m) = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
mi = min(a)
ma = max(a)
k = min(b)
if 2 * mi <= ma:
    v = ma
else:
    v = 2 * mi
if v >= k:
    print(-1)
else:
    print(v)
