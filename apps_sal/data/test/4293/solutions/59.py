(p, q, r) = map(int, input().split())
n = p + q + r
n -= max(p, q, r)
print(n)
