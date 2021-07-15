n = int(input())
ans = (n - 1) // 3 * 2 + int(n % 3 == 0) + 1
print(ans)

