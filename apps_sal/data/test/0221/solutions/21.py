n, k = map(int, input().split())
a = 1000000
af = []
for i in range(k+1):
    f = []
    for j in range(i+1, n+1, 2*k+1):
        f.append(j)
    if i+1 > n:
        break
    if f[-1]+k >= n:
        if a > len(f):
            a = len(f)
            af = f[:]
print(a)
print(*af)
