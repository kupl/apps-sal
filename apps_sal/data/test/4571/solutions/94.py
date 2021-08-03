n, m = map(int, input().split())
res = 2**m
ans = 1900 * m + 100 * (n - m)
print(ans * res)
