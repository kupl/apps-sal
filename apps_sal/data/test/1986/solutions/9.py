n, k = list(map(int, input().split()))
a = -1 << 30
for i in range(n):
    f, t = list(map(int, input().split()))
    if t > k:
        f -= t - k
    a = max(a, f)

print(a)
