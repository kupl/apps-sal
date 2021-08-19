(w, l) = list(map(int, input().split()))
a = list(map(int, input().split()))
r = 1e+18
s = sum(a[:l])
for i in range(l, w - 1):
    r = min(s, r)
    s += a[i]
    s -= a[i - l]
r = min(s, r)
print(r)
