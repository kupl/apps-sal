n = int(input())
a = list(map(int, input().split()))
a = [a[i % n] for i in range(0, 2 * n, 2)]
s1 = sum(a[:(n + 1) // 2])
sx = s1
for i in range(1, n):
    s1 += a[(i + (n - 1) // 2) % n] - a[i - 1]
    sx = max(sx, s1)
print(sx)
