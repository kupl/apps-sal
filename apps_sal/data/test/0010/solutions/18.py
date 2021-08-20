n = int(input())
a = n // 7 * 2
print(a + max(0, n % 7 - 5), a + min(2, n % 7))
