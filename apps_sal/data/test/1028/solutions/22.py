n, m = list(map(int, input().split()))
d = n // m
ans1 = ((n % m) * (d + 1) * d / 2) + (m - n % m) * d * (d - 1) / 2
ans2 = (n - m + 1) * (n - m) // 2
print(int(ans1), int(ans2))
