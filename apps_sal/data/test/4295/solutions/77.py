n, m = map(int, input().split())
tmp = n % m
print(min(tmp, abs(tmp - m)))
