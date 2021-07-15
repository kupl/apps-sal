n = int(input())
mx = list(map(float, input().split()))
mn = list(map(float, input().split())) + [0]

for i in range(1, n):
    mx[i] += mx[i - 1]
for i in range(n - 2, -1, -1):
    mn[i] += mn[i + 1]

a, b = [0] * (n + 1), [0] * (n + 1)
for i in range(n):
    p = mx[i]
    s = 1 + mx[i] - mn[i + 1]
    a[i] = (s - max(s * s - 4 * p, 0) ** 0.5) / 2
    b[i] = (s + max(s * s - 4 * p, 0) ** 0.5) / 2
print(*(a[i] - a[i - 1] for i in range(n)))
print(*(b[i] - b[i - 1] for i in range(n)))
