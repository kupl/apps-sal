n = int(input())
yes = 0
breaker = 0
for a in range(n // 1234567 + 1):
    for b in range((n - a * 1234567) // 123456 + 1):
        y = 1234567 * a + 123456 * b
        if (n - y) % 1234 == 0:
            yes = 1
            print('YES')
            breaker = 1
            break
    if breaker == 1:
        break
if yes == 0:
    print('NO')
