n = int(input())
x = n // 7 * 2
print(x + (n % 7 == 6), x + min(n % 7, 2))
