n, m = map(int, input().split())
ans = int((1900 * m + 100 * (n - m)) / ((1 / 2) ** m))
print(ans)
