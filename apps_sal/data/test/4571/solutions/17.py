n, m = map(int, input().split())
x = 1900 * m + 100 * (n - m)
ans = x * 2**m
print(ans)
