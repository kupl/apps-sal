n = int(input())
a = list(map(int, input().split()))
m = float('inf')
for x in range(n):
    e = 0
    for f in range(n):
        e += a[f] * (abs(x - f) + f + x) * 2
    m = min(e, m)
print(m)
