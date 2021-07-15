x, y = map(int, input().split())
b = y // x
if y % x != 0:
    print(0);return
ds = set()
M = 10**9 + 7
for i in range(1, int(pow(b,0.5)+1)):
    if b % i == 0:
        ds.add(i)
        ds.add(b//i)
ds = sorted(list(ds))
ans = pow(2, b-1, M)
f = ds[::]
for i in range(len(ds)):
    f[i] = pow(2, ds[i]-1, M)
    for j in range(i):
        if ds[i] % ds[j] == 0:
            f[i] -= f[j]
print(f[-1]%M)
