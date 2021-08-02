import sys
n, m = list(map(int, input().split()))
a = 0
s = n * n // 4 if n % 2 == 0 else (n // 2) * (n // 2 + 1)
t = n * (n - 1) // 2
for _ in range(m):
    x, d = list(map(int, sys.stdin.readline().split()))
    a += (x * n) + (s * d if d < 0 else t * d)
print(a / n)
