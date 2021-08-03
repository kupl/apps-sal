n, k = list(map(int, input().split()))

p = 0
for _ in range(n):
    l, r = list(map(int, input().split()))
    p += r - l + 1

print(0) if k % p == 1 else print((k - (p % k)) % k)
