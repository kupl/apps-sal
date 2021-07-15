w, l = map(int, input().split())
a = list(map(int, input().split()))
f = s = sum(i for i in a[:l])
for i, b in enumerate(a[l:]):
    s += b - a[i]
    f = min(s, f)
print(f)
