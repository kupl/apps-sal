n, k = tuple(map(int, input().split()))

q = n // k

while q * k <= n:
    q += 1

print(q * k)
