n, m = map(int, input().split())

t = m * 1900 + (n - m) * 100
ans = t * (2 ** m)

print(ans)
