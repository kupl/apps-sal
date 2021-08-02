n, m = map(int, input().split())
x = list(map(int, input().split()))
y = list(map(int, input().split()))
M, a, b = 10**9 + 7, 0, 0
for i in range(n):
    a += (2 * i - n + 1) * x[i]
    a %= M
for i in range(m):
    b += (2 * i - m + 1) * y[i]
    b %= M
print(a * b % M)
