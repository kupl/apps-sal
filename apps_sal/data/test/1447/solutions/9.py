(n, m) = map(int, input().split())
t = m * n
print(1 if t == 1 else (2 * t - (m + n)) / (n * (t - 1)))
