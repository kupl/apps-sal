(n, m) = list(map(int, input().split()))
ans = 0
ans += pow(2, m) * (1900 * m + 100 * (n - m))
print(ans)
