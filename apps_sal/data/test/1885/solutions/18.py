n = int(input())
ans = n * (n - 1) * (n - 2) * (n - 3) * (n - 4) * (n - 5) * (n - 6) // (120 * 6 * 7)
ans += n * (n - 1) * (n - 2) * (n - 3) * (n - 4) * (n - 5) // (120 * 6)
ans += n * (n - 1) * (n - 2) * (n - 3) * (n - 4) // 120
print(ans)
