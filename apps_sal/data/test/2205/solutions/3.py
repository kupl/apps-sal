(n, p) = (int(input()), list(map(int, input().split())))
(s, q) = (0, list(range(n + 1)))
for i in range(1, n + 1):
    q[i] ^= q[i - 1]
    if n // i & 1:
        s ^= q[i - 1]
    s ^= q[n % i]
for i in p:
    s ^= i
print(s)
