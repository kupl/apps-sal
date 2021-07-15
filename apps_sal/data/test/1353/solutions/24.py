n, m, a, b = map(int, input().split())
s1 = a * n
s2 = n // m * b + n % m * a
s3 = (n + m - 1) // m * b
print(min(s1, s2, s3))
