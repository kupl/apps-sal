n = int(input())
print(-1 if n < 3 else 10 ** (n - 1) // 210 * 210 + 210)
