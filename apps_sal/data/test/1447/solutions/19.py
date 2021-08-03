S = str(input())
l = list(map(int, S.split(' ')))
n, m = l[0], l[1]
S = 0
t = 1 / n
l = m * n - m - n
y = min(n, m)
z = max(n, m)
for i in range(1, y + 1):
    if i > 1:
        t = t * i * (m + 1 - i) * (m * n - z - i + 2) * (n + 1 - i) / ((i - 1) * (i - 1) * (l + i) * (n * m - i + 1))
    S = S * (m * n - z - i + 2) / (n * m - i + 1) + t
print(S)
