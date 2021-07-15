n = int(input())
V = E = 0
for d in range(1,n+1): V += d * (d + 1) // 2
for _ in range(n-1):
    a, b = list(map(int, input().split()))
    if a > b: a, b = b, a
    E += a * (n - b + 1)
print((V - E))

