n, m = map(int, input().split())

submit = 1900 * m + 100 * (n - m)

ans = submit * 2**m
print(ans)
