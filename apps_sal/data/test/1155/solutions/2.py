r = lambda: map(int, input().split())
n, m = r()
s = 10E10

for _ in range(n):
    a, b = r()
    s = min(s, a / b)

print(s * m)
