input()
ds = list(map(int, input().split()))
x = max(ds)
for v in {v for v in ds if x % v == 0}:
    ds.remove(v)
y = max(ds)
print(x, y)
