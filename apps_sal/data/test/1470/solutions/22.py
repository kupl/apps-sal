x = int(input())
ans = x // 11 * 2
print(ans + (x % 11 > 0) + (x % 11 > 6))
