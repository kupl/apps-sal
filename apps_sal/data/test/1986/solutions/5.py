(n, k) = list(map(int, input().split()))
x = -100000000000000
for i in range(n):
    (f, t) = list(map(int, input().split()))
    if t > k:
        x = max(x, f + k - t)
    else:
        x = max(x, f)
print(x)
