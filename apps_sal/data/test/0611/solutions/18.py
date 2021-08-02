n, m = list(map(int, input().split()))
t = n // 2
s = 0
for i in range(m):
    a, b = list(map(int, input().split()))
    if b < 0:
        if n % 2:
            s += b * t * (t + 1)
        else:
            s += b * t * (t - 1) // 2 + b * (t + 1) * t // 2
    if b > 0:
        s += b * n * (n - 1) // 2
    s += n * a

print(s / n)
