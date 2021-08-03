n, m, a, b = [int(x) for x in input().split()]

res = (n % m) * b
res = min(res, ((m - (n % m)) % m) * a)

print(res)
