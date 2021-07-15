n, m = map(int, input().split())
base = m * 1900 + (n - m) * 100
case = pow(2, m)
print(base * case)
