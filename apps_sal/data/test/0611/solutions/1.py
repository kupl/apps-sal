n, m = list(map(int, input().split()))
a = (n * (n - 1)) // 2
n2 = n // 2
b = n2 * (n2 + 1)
if n % 2 == 0:
    b -= n2
s = 0
for i in range(m):
    x, d = list(map(int, input().split()))
    s += x * n
    s += d * (a if d > 0 else b)

print(s / n)
