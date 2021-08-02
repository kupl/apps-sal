n = int(input())

if n % 2 == 1:
    print(n // 2 * 3 + 1)
else:
    print(n // 2 * 3)

print(*range(2, n + 1, 2), end=' ')
print(*range(1, n + 1, 2), end=' ')
print(*range(2, n + 1, 2), end=' ')
