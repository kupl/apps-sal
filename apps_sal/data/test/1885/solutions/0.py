n = int(input())
ans = 0
ans = ans + n * (n - 1) * (n - 2) * (n - 3) * (n - 4) // (2 * 3 * 4 * 5)
ans = ans + n * (n - 1) * (n - 2) * (n - 3) * (n - 4) * (n - 5) // (2 * 3 * 4 * 5 * 6)
ans = ans + n * (n - 1) * (n - 2) * (n - 3) * (n - 4) * (n - 5) * (n - 6) // (2 * 3 * 4 * 5 * 6 * 7)
print(ans)
