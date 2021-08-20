(n, k) = list(map(int, input().split()))
print((n * 6 - 1) * k)
for i in range(n):
    m = i * 6
    print((m + 1) * k, (m + 2) * k, (m + 3) * k, (m + 5) * k)
