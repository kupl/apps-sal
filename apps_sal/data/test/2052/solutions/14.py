w, l = list(map(int, input().split()))
a = list(map(int, input().split()))
s = sum(a[:l])
r = 1000000000000000000
r = min(s, r)
for i in range(w - l - 1):
    s += a[i + l]
    s -= a[i]
    r = min(s, r)
print(r)
