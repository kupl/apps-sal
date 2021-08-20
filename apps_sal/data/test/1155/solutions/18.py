(n, m) = [int(z) for z in input().split()]
tmp = 10000000
for i in range(n):
    (a, b) = [int(z) for z in input().split()]
    tmp = min(tmp, a / b)
print(tmp * m)
