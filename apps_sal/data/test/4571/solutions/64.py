(n, m) = list(map(int, input().split()))
exp = 2 ** m
ans = exp * (1900 * m + 100 * (n - m))
print(ans)
